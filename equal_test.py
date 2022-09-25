import unittest


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        firstvalue = "hello world"
        secondvalue = "hello World"
        result = "Both firstvalue and secondvalue are equal "
        self.assertEqual(firstvalue, secondvalue, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
