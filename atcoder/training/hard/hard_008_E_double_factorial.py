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
        input = """12"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000000000000"""
        output = """124999999999999995"""
        self.assertIO(input, output)

def resolve():
  N = int(input())

  if N%2:
    print(0)
    return True
  multiplier = 10
  result = 0
  while multiplier <= N:
    result += N // multiplier
    multiplier *= 5

  print(result)

# if __name__ == "__main__":
#   resolve()


if __name__ == "__main__":
    unittest.main()
