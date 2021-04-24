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
        input = """cabacc
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """codeforces
atcoder"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  T = list(input())

  min_count = len(T)
  for i in range(len(S) - len(T) + 1):
    temp_counter = 0
    for t in range(len(T)):
      if T[t] != S[i + t]:
        temp_counter += 1
    if temp_counter < min_count:
      min_count = temp_counter

  print(min_count)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
