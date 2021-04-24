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
        input = """5
2 1 5 4 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 3 3 3 3"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  result = 0
  for i in range(1, N):
    if A[i-1] > A[i]:
      result += A[i-1] - A[i]
      A[i] = A[i-1]
  print(result)
if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
