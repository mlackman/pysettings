import unittest
import os


from pysett import settings

class TestSettings(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.yaml')

    def test_test_env_settings(self):
        s = settings.create(env='test', settings=self.filename)
        self.assertEquals(s.value, 7)
        self.assertEquals(s.setting, 1)
        self.assertEquals(s.somecomp.username, 'uname')
        self.assertEquals(s.somecomp.password, 'pword')

    def test_production_env_settins(self):
        s = settings.create(env='production', settings=self.filename, secrets={'production':self.production_secret_settings})

        self.assertEquals(s.value, 5)
        self.assertEquals(s.setting, 2)
        self.assertEquals(s.somecomp.username, 'mysecretusername')
        self.assertEquals(s.somecomp.password, 'mysecretpassword')

    @property
    def production_secret_settings(self):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'production_secret.yaml')







