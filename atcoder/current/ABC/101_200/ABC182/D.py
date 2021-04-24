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
2 -1 -2"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
-2 1 3 -1 -1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
-1000 -1000 -1000 -1000 -1000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  ans = 0
  max_sum_a = 0
  sum_a = 0
  now = 0
  for a in A:
    sum_a += a
    max_sum_a = max(sum_a, max_sum_a)
    ans = max(now+max_sum_a, ans)
    now += sum_a
  print(ans)


resolve()

if __name__ == "__main__":
    unittest.main()
