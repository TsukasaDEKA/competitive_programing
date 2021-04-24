import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_Sample_Input_1(self):
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)

from math import cos
from math import radians
from math import sqrt

def hour2deg(hour, min):
  return hour*30 + min/2

def min2deg(min):
  return min*6

def resolve():
  A, B, H, M = map(int, input().split(" "))
  degree = abs(hour2deg(H, M) - min2deg(M))
  if degree > 180:
    degree = 360.0 - degree
  length = sqrt(A**2 + B**2 - 2*A*B*cos(radians(degree)))
  print(length)

# if __name__ == "__main__":
#     resolve()

if __name__ == "__main__":
    unittest.main()