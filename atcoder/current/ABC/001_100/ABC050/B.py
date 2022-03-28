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
2 1 4
2
1 1
2 3"""
        output = """6
9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
7 2 3 8 5
3
4 2
1 7
4 13"""
        output = """19
25
30"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  T = [int(x) for x in input().split(" ")]
  sumT = sum(T)
  M = int(input())
  for i in range(M):
    p, x = [int(x) for x in input().split(" ")]
    print(sumT-T[p-1]+x)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()