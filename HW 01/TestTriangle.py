#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import unittest


def classify_triangle(a, b, c):
    sides = [a, b, c]
    for i in sides:
        try:
            num = int(i)
        except ValueError:
            flag = False
            return "Wrong input"
        else:
            flag = True

    while flag:
        sides.sort()
        a = sides[0]
        b = sides[1]
        c = sides[2]

        if a + b <= c:
            return "Not a triangle"
        elif a == b and b != c:
            return "Isosceles"
        elif a == b == c:
            return "Equilateral"
        elif a != b and a != c and a * a + b * b == c * c:
            return "Right"
        else:
            return "Scalene"


class TestTriangles(unittest.TestCase):
    def testSet(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
        self.assertEqual(classify_triangle(1, 2, 1), "Not a triangle")
        self.assertEqual(classify_triangle(1, 3, 1), "Not a triangle")
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")
        self.assertEqual(classify_triangle(4, 4, 7), "Isosceles")
        self.assertEqual(classify_triangle(3, "y", 5), "Wrong input")


if __name__ == '__main__':
    unittest.main(exit=False)
    print(classify_triangle(5, 12, 13))
    print(classify_triangle(4, 2, 1))
    print(classify_triangle(4, 2, 2))
    print(classify_triangle(3, 3, 3))
    print(classify_triangle(5, 6, 7))
    print(classify_triangle(5, 9, 5))
    print(classify_triangle(7, "y", 6))
