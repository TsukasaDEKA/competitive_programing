import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
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
2 3 1"""
        output = """3 1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 2 3"""
        output = """1 2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
5 3 2 4 1"""
        output = """5 3 2 4 1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  P = [int(x) for x in input().split(" ")]

  ans = [0]*N
  for i in range(N):
    ans[P[i]-1] = i+1
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()