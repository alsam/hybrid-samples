import unittest
# import our `pybind11`-based extension module from package framegrabber
import vossen

class MainTest(unittest.TestCase):
    def test_add(self):
        # test that 1 + 1 = 2
        self.assertEqual(vossen.add(1, 1), 2)

    def test_subtract(self):
        # test that 1 - 1 = 0
        self.assertEqual(vossen.subtract(1, 1), 0)

if __name__ == '__main__':
    unittest.main()

