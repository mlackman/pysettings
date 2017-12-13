import os
from typing import List

import yaml


def dict_updater(source: dict, dest: dict) -> dict:
    """
    Updates source dict with target dict values creating
    new dict and returning it
    """
    target = dest.copy()

    for k, v in source.items():
        if isinstance(v, dict) and k in dest:
            target[k] = dict_updater(v, dest[k])
        else:
            target[k] = v
    return target


class Object():
    pass


class ObjectFactory():

    def __init__(self, d: dict):
        self.d = d

    def create(self):
        obj = Object()
        for k, v in self.d.items():
            if isinstance(v, dict):
                obj.__dict__[k] = ObjectFactory(v).create()
            else:
                obj.__dict__[k] = v
        return obj


class SettingsObjectFactory():

    def __init__(self, settings: dict):
        self.settings = settings

    def get_settings(self, env: str):
        common_settings = self.settings.get('common', {})
        env_specific_settings = self.settings[env]

        env_settings = dict_updater(env_specific_settings, common_settings)
        return ObjectFactory(env_settings).create()


class EnvironmentVariables():

    def __init__(self, environment_vars: dict):
        self._vars = {}
        keys = filter(lambda k: k.startswith('settings.'), environment_vars.keys())
        for k in keys:
            self._vars[k] = environment_vars[k]

    def to_dict(self):
        d = {}
        for k, v in self._vars.items():
            keys = k.split('.')[1:]  # ignore the 'settings' from start
            d = dict_updater(d, (self._create_dict_from_keys(keys, v)))
        return d

    def _create_dict_from_keys(self, setting_keys: List[str], value) -> dict:
        d = {setting_keys[-1]: value}
        del setting_keys[-1]
        if len(setting_keys) > 0:
            d = self._create_dict_from_keys(setting_keys, d)
        return d


def create(env: str, settings: str, secrets: dict=None):
    """
    Creates setting object, which has properties from the settings file.
    secrets dict can contain environment specific secrets, which are updated to
    settings.
    environment variables overrides everything. Setting specific environment variable
    must be like settings.somecomp.username
    """
    with open(settings, 'rt') as f:
        settings_data = yaml.load(f.read())
        settings_data = _override_with_secrets(env, settings_data, secrets)
        settings_data = _override_with_environment_variables(env, settings_data)

    return SettingsObjectFactory(settings_data).get_settings(env)


def _override_with_secrets(env: str, settings_data: dict, secrets: dict) -> dict:
    if secrets and env in secrets:
        with open(secrets[env], 'rt') as f:
            secret_data = yaml.load(f.read())
        env_settings_with_secrets = dict_updater(secret_data, settings_data[env])
        settings_data[env] = env_settings_with_secrets
    return settings_data


def _override_with_environment_variables(env: str, settings_data: dict) -> dict:
    env_vars = EnvironmentVariables(os.environ)
    env_settings_with_env_override = dict_updater(env_vars.to_dict(), settings_data[env])
    settings_data[env] = env_settings_with_env_override
    return settings_data
