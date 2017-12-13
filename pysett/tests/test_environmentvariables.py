import unittest

from pysett.settings import EnvironmentVariables


class TestEnvironmentVariables(unittest.TestCase):

    def test_main_level_variable(self):
        env = {'settings.value': 1}

        env_vars = EnvironmentVariables(env)

        self.assertDictEqual({'value': 1}, env_vars.to_dict())

    def test_few_main_level_variables(self):
        env = {'settings.value': 1, 'settings.other_value': 2}
        env_vars = EnvironmentVariables(env)
        self.assertDictEqual({'value': 1, 'other_value': 2}, env_vars.to_dict())

    def test_deep_variables(self):
        env = {'settings.comp.value': 1}

        env_vars = EnvironmentVariables(env)

        self.assertDictEqual({'comp': {'value': 1}}, env_vars.to_dict())

    def test_deep_variables(self):
        env = {
            'settings.comp.value': 1,
            'settings.comp.other_value': 2,
        }

        env_vars = EnvironmentVariables(env)

        expected_dict = {'comp': {'value': 1, 'other_value': 2}}

        self.assertDictEqual(expected_dict, env_vars.to_dict())

    def test_complex(self):
        env = {
            'settings.comp.value': 1,
            'settings.comp.other_value': 2,
            'settings.comp.comp2.value': 1,
            'settings.comp.comp2.value_2': 1,
            'settings.value': 5,
        }

        env_vars = EnvironmentVariables(env)

        expected_dict = {
                'comp': {'value': 1, 'other_value': 2, 'comp2': {'value': 1, 'value_2': 1}},
                'value': 5
        }

        self.assertDictEqual(expected_dict, env_vars.to_dict())
