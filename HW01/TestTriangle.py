import unittest


def classify_triangle(a_side, b_side, c_side):
    """This function is used to judge the type of the triangle"""
    sides = [a_side, b_side, c_side]
    for i in sides:
        try:
            int(i)
        except ValueError:
            flag = False
            return "Wrong input"
        else:
            flag = True

    while flag:
        sides.sort()
        a_side = sides[0]
        b_side = sides[1]
        c_side = sides[2]

        if a_side <= 0 or b_side <= 0 or c_side <= 0 or a_side + b_side <= c_side:
            return "Not a triangle"
        if a_side == b_side and b_side != c_side:
            return "Isosceles"
        if a_side == b_side == c_side:
            return "Equilateral"
        if a_side != b_side and a_side != c_side \
                and a_side * a_side + b_side * b_side == c_side * c_side:
            return "Right"
        return "Scalene"


class TestTriangles(unittest.TestCase):
    """This is the unittest class"""

    def test_set(self):
        """This is the test cases of the unittest"""
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
        self.assertEqual(classify_triangle(1, 2, 1), "Not a triangle")
        self.assertEqual(classify_triangle(1, 3, 1), "Not a triangle")
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")
        self.assertEqual(classify_triangle(4, 4, 7), "Isosceles")
        self.assertEqual(classify_triangle(3, "y", 5), "Wrong input")
        self.assertEqual(classify_triangle(-3, -4, -5), 'Not a triangle')


if __name__ == '__main__':
    unittest.main(exit=False)
    print(classify_triangle(5, 12, 13))
    print(classify_triangle(4, 2, 1))
    print(classify_triangle(4, 2, 2))
    print(classify_triangle(3, 3, 3))
    print(classify_triangle(5, 6, 7))
    print(classify_triangle(5, 9, 5))
    print(classify_triangle(7, "y", 6))
