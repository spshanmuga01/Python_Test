import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(True,True)  # add assertion here
    def test_two(self):
        self.assertEqual(True,True)
    def test_three(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
