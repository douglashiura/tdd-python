'''
Created on May 27, 2019

@author: douglas
'''
import unittest

import numpy as np


class Test(unittest.TestCase):

    def testPrint(self):
        a = np.array([[1, 2], [3, 4]])
        print(a)
    def testAdd1(self):
        a = np.array([[1, 2], [3, 4]]);
        a=a+1;
        self.assertEquals(2, a[0][0])
        self.assertEqual(2, len(a))