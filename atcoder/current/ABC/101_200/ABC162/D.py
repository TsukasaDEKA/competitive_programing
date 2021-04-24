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
RRGB"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"""
        output = """1800"""
        self.assertIO(input, output)

import itertools
def resolve():
  N = int(input())
  S = list(input())

  color_count = {
    'R': 0,
    'G': 0,
    'B': 0,
  }

  for color in S:
    color_count[color] += 1
  all_pattarn = color_count["R"] * color_count["G"] * color_count["B"]

  count = 0
  for i in range(N-2):
    for j in range(1, int((N-i-1)/2)+1):
      if S[i] != S[i+j] and S[i] != S[i+2*j] and S[i+j] != S[i+2*j]: count+=1
  print(all_pattarn - count)


resolve()

if __name__ == "__main__":
    unittest.main()