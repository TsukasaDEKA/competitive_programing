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
        input = """1
10
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
9
3 6"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
20
11 12 9 17 12"""
        output = """74"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  K = int(input())
  A = [int(x) for x in input().split(" ")]
  ans = 0
  for i in range(N):
    ans += 2*min(A[i], K-A[i])

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()