import unittest


class MyTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertTrue('hello world'.upper(), "HELLO WORLD")
        #self.assertFalse('hello world'.upper(), "Hello World")
    def test_split(self):
        self.assertTrue('Hello World'.split(), ['Hello', 'World'])


if __name__ == '__main__':
    unittest.main()
