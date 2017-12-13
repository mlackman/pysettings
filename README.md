# pysettings
Simple yaml settings configuration

# How to use

Define the settings files

All the settings can be overwritten by environment variables. Overwrite can be done with env var like
settings.somecomp.username=myusername

settings.yaml

```YAML
common:
    value: 5
test:
    value: 7
    setting: 1
    somecomp:
        username: uname
        password: pword

production:
    setting: 2
    somecomp:
        username: secret
        password: secret
```

production_secrets.yaml

```YAML
somecomp:
    username: mysecretusername
    password: mysecretpassword
```

settings.py

```python
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.yaml')
production_secrets = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'production_secret.yaml')

s = settings.create(env='production', settings=filename, secrets={'production':self.production_secrets})

assert s.value == 5
assert s.setting == 2
assert s.somecomp.username == 'mysecretusername'
assert s.somecomp.password == 'mysecretpassword'
```


