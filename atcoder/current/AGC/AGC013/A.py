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
        input = """6
1 2 3 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9
1 2 1 2 1 2 1 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
1 2 3 2 1 999999999 1000000000"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 適当にやるとバグらせそう。
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  count = 1
  direction = 0
  for i in range(1, N):
    diff = A[i] - A[i-1]
    if direction == 0:
      direction = diff
    elif direction * diff < 0:
      count+=1
      direction = 0

  print(count)

resolve()

if __name__ == "__main__":
    unittest.main()
