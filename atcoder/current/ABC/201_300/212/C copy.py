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
        input = """2 2
1 6
4 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18
  N, M = map(int, input().split(" "))
  A = [(int(x), "A") for x in input().split(" ")]
  B = [(int(x), "B") for x in input().split(" ")]

  C = sorted(A+B)
  ans = inf
  for i in range(N+M-1):
    if C[i][1] != C[i+1][1]:
      ans = min(ans, abs(C[i][0]-C[i+1][0]))

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()