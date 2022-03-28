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
        input = """abcdef
2
3 5
1 4"""
        output = """debacf"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """redcoat
3
1 7
1 2
3 4"""
        output = """atcoder"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = list(input())
  N = int(input())
  for _ in range(N):
    l, r = [int(x)-1 for x in input().split(" ")]
    S = S[:l] + S[l:r+1][::-1] + S[r+1:]

  print("".join(S))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()