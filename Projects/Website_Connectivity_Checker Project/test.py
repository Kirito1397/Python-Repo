'''
The benefit of using __import__() is that you don’t have to turn your project folder into a package, and you can specify the file name.
This is also useful if your filename collides with any standard library packages. For example, math.py would collide with the math module.
'''
import unittest
import os, sys

import sys
sys.path.append("C:/Users/Kirito/Desktop/Programming Codes/Code Repo/Python Repo/Projects/Website_Connectivity_Checker Project/website_connectivity_checker")

from website_connectivity_checker import __main__

class test_main(unittest.TestCase):

    def test_sum(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"

    def test_main(self):
        self.main()
        
        self.assertTrue()


if __name__ == "__main__":
    unittest.main()