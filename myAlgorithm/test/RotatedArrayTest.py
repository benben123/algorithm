import unittest

from myAlgorithm.py.RotatedArray import RotatedArray


class TestRotatedArrayMethod(unittest.TestCase):
    def testRotateAarry(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        test = RotatedArray().rotate(nums,k)
        print test
        self.assertEqual(test, [5,6,7,1,2,3,4])


if __name__ == "__main__":
    unittest.main()

