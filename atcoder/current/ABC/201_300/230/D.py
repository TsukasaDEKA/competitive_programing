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
        input = """3 3
1 2
4 7
5 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
1 2
4 7
4 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 2
1 100
1 1000000000
101 1000
9982 44353
1000000000 1000000000"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 最後に打ったパンチだけ覚えておく。
  inf = 10**18+1
  N, D = map(int, input().split(" "))
  L_R = sorted([[int(x) for x in input().split(" ")] for _ in range(N)], key=lambda x: x[1])
  ans = 0
  last = 0
  for i in range(N):
    l, r = L_R[i]
    if last < l:
      ans+=1
      last = r+D-1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()