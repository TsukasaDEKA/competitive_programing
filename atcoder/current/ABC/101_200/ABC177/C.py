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
        input = """3
1 2 3"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
141421356 17320508 22360679 244949"""
        output = """437235829"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  # sumA = sum(A)
  reversedIntegraA = [0] * len(A)
  reversedIntegraA[-1] = A[-1]
  base = 10**9+7

  for i in reversed(range(len(A) - 1)):
    reversedIntegraA[i] = reversedIntegraA[i+1] + A[i]

  result = 0
  for i in range(len(A) - 1):
    result += A[i] * reversedIntegraA[i+1]
    if result > base:
      result %= base
  print(result)


if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
