import unittest


class MyTestCase(unittest.TestCase):
    def test_in(self):
        key = "sentence"
        container = "This the first sentence of the test programe"
        result = "yes,the word is in the container.."
        #return OK if word sentence is in the container
        self.assertIn(key, container, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
