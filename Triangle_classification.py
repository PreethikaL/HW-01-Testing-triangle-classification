import unittest

class ClassifyTriangle:
    def classify_triangle(a,b,c) :
        result = ""
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            result = "Right triangle"
        elif a == b and b == c and c == a :
            result = "Equilateral triangle"
        elif a == b or b == c or c == a :
            result = "Isoceles triangle"
        elif a !=b and a!=c and b!= c :
            result = "Scalene triangle"
        elif a + b <= c or b+c<=a  or c+a<=b :
            result = "this would not form a triangle"

        return result


class TestTriangles(unittest.TestCase):
    def testRight(self):
        try:
            self.assertNotEqual(ClassifyTriangle.classify_triangle(3, 4, 5),
                                'Equilateral triangle', 'Should be Right')
        except AssertionError:
            print("Assertion error")

    def testEquilateral(self):
        try:
            self.assertEqual(ClassifyTriangle.classify_triangle(7, 7, 7),
                             'Equilateral triangle', '7,7,7 is an Equilateral triangle')
        except AssertionError:
            print("Assertion error")

    def testIsoceles(self):
        try:
            self.assertEqual(ClassifyTriangle.classify_triangle(5, 5, 4),
                             'Isoceles triangle', '7,7,7 is an Equilateral triangle')
        except AssertionError:
            print("Assertion error")

    def testScalene(self):
        try:
            self.assertNotEqual(ClassifyTriangle.classify_triangle(2, 3, 4),
                             'Equilateral triangle', '7,7,7 is an Equilateral triangle')
        except AssertionError:
            print("Assertion error")


if __name__ == '__main__':
    # examples of running the code
    # ClassifyTriangle.classify_triangle(1, 2, 3)
    # ClassifyTriangle.classify_triangle(1, 1, 1)

    unittest.main(exit=False)


    # print("enter the three sides: ")
    # a = int(input("a: "))
    # b = int(input("b: "))
    # c = int(input("c: "))


