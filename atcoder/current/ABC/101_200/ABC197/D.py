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
        input = """4
1 1
2 2"""
        output = """2.00000000000 1.00000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
5 3
7 4"""
        output = """5.93301270189 2.38397459622"""
        self.assertIO(input, output)

def resolve():
  # 中点？
  from math import sin, cos, sqrt, pi, radians

  N = int(input())
  x_0, y_0 = map(int, input().split(" "))
  x_op, y_op = map(int, input().split(" "))
  x_cent, y_cent = (x_0+x_op)/2, (y_0+y_op)/2
  sita = radians(360/N)
  x = (x_0-x_cent)*cos(sita)-(y_0-y_cent)*sin(sita)+x_cent
  y = (x_0-x_cent)*sin(sita)+(y_0-y_cent)*cos(sita)+y_cent
  print(x, y)

resolve()

if __name__ == "__main__":
    unittest.main()
