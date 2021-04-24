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
        input = """20"""
        output = """0
0
0
0
0
1
0
0
0
0
3
0
0
0
0
0
3
3
0
0"""
        self.assertIO(input, output)

import math

def resolve():
  N = int(input())

  result = [0] * (N + 1)
  max_range = int(math.sqrt(N)) + 1
  for x in range(1, max_range):
    for y in range(1, max_range):
      for z in range(1, max_range):
        index = x**2 + y**2 + z**2 + x*y + y*z + z*x
        if index <= N:
          # if index == 8:
          #   print("x: {0}, y: {1},z: {2},".format(x, y, z))
          result[index] += 1

  for i in result[1:]:
    print(i)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
