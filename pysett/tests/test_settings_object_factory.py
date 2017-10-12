import unittest

from pysett.settings import SettingsObjectFactory


class TestSettingsObjectFactory(unittest.TestCase):


    def test_two_envs(self):
        settings = {
            'test': {
                'value': 5,
                'other': 4
            },
            'dev': {
                'value': 7,
                'other': 6
            }
        }
        of = SettingsObjectFactory(settings)

        obj = of.get_settings('test')
        self.assertEquals(obj.value, 5)
        self.assertEquals(obj.other, 4)

        obj = of.get_settings('dev')
        self.assertEquals(obj.value, 7)
        self.assertEquals(obj.other, 6)

    def test_common_values(self):
        settings = {
            'common': {
                'common_value': 'some'
            },
            'test': {
                'value': 5,
                'other': 4
            },
            'dev': {
                'value': 7,
                'other': 6,
                'common_value': 'something else'
            }
        }

        of = SettingsObjectFactory(settings)
        obj = of.get_settings('test')
        self.assertEquals(obj.value, 5)
        self.assertEquals(obj.other, 4)
        self.assertEquals(obj.common_value, 'some')

        obj = of.get_settings('dev')
        self.assertEquals(obj.value, 7)
        self.assertEquals(obj.other, 6)
        self.assertEquals(obj.common_value, 'something else')










