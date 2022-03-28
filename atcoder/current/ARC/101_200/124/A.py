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
        input = """3 2
L 1
R 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """30 10
R 6
R 8
R 7
R 25
L 26
L 13
R 14
L 11
L 23
R 30"""
        output = """343921442"""
        self.assertIO(input, output)


def resolve():
  mod = 998244353
  # N が小さいのでO(N**2)でいける。
  N, K = map(int, input().split(" "))
  R = [-1]*N
  L = [-1]*N
  table = [-1]*N
  for i in range(K):
    C, k = input().split(" ")
    k = int(k)-1
    # 固定
    table[k] = i
    if C == "R": R[k] = i
    else: L[k] = i
  
  ans = 1
  for i in range(N):
    if table[i] == -1:
      count = len([x for x in R[:i] if x >=0])+len([x for x in L[i:] if x >=0])
      ans*=(K-count)
      if ans>=mod: ans%=mod
      
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()