import unittest
# import our `pybind11`-based extension module from package framegrabber
import vossen
import numpy as np

class MainTest(unittest.TestCase):
    def test_add(self):
        # test that 1 + 1 = 2
        self.assertEqual(vossen.add(1, 1), 2)

    def test_subtract(self):
        # test that 1 - 1 = 0
        self.assertEqual(vossen.subtract(1, 1), 0)

    def test_cosfft1(self):
        # v = vossen.VectorDouble([1,2,3])
        # v1 = vossen.VectorDouble([6,-2,2])
        v = np.array([1.,2,3])
        v1 = np.array([6.,-2,2])
        vossen.cosfft1(v, 2)
        # self.assertAlmostEqual(v, v1)
        self.assertTrue(np.allclose(v, v1))
        vossen.cosfft1(v, 2, inverse = True)
        # self.assertAlmostEqual(v, vossen.VectorDouble([1.,2,3]))
        self.assertTrue(np.allclose(v, np.array([1.,2,3])))

    def test_cft2(self):
        m = m_orig = np.array([[1.,2,3],
                               [4,5,6],
                               [7,8,9]])
        m1 = np.array([[ 6.,  4., 10.],
                       [18., 10., 22.],
                       [30., 16., 34.]])
        vossen.cft2(m, 2)
        self.assertTrue(np.allclose(m, m1))
        vossen.cft2(m, 2, inverse = True)
        self.assertTrue(np.allclose(m, m_orig))

    def test_scale_by_2(self):
        x = np.array([1.,2.,3.,])
        vossen.scale_by_2(x)
        self.assertTrue(np.allclose(x, np.array([2., 4., 6.])))

if __name__ == '__main__':
    unittest.main()

