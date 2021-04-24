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
        input = """2
1 3
3 5"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
11 13
17 47
359 44683"""
        output = """998244353"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
1 1000000"""
        output = """500000500000"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  ans = 0
  for _ in range(N):
    A, B = map(int, input().split(" "))
    n = B-A+1
    # if n%2:
    #   sum_a_b = n*int((A+B)/2)
    # else:
    #   sum_a_b = int(n/2)*(A+B)
    ans += int(n*(A+B)/2)
  print(ans)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
