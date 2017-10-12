import unittest

from pysett.settings import ObjectFactory


class TestObjectFactory(unittest.TestCase):

    def create(self, d:dict):
        of = ObjectFactory(d)
        return of.create()

    def test_simple(self):
        obj = self.create({'m':5})

        self.assertEquals(obj.m, 5)

    def test_few_properties(self):
        obj = self.create({'m':5, 'a':'m'})

        self.assertEquals(obj.m, 5)
        self.assertEquals(obj.a, 'm')

    def test_deebly_nested_dicts(self):
        obj = create({'m':{'b':1, 'c':{'d':3}}, 'a':'m'})

        self.assertEquals(obj.m.b, 1)
        self.assertEquals(obj.m.c.d, 3)
        self.assertEquals(obj.a, 'm')

    def test_list(self):
        obj = self.create({'m':5, 'a':[1,2,3]})

        self.assertEquals(obj.m, 5)
        self.assertEquals(obj.a, [1,2,3])









