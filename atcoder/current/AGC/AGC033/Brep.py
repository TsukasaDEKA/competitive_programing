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
        input = """2 3 3
2 2
RRL
LUD"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 3 5
2 2
UDRRR
LLDUD"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9 3 5
1 1
DDLLR
RRUUU"""
        output = """YES"""
        self.assertIO(input, output)

def resolve():
  # RLUD それぞれで集計して累積和をとる。
  inf = 10**18+1
  H, W, N = map(int, input().split(" "))
  H_, W_ = [int(x)-1 for x in input().split(" ")]
  S = list(input())
  T = list(input())
  pair = [["R", "L"], ["L", "R"], ["D", "U"], ["U", "D"]]
  diff = [[W-W_, W], [W_+1, W], [H-H_, H], [H_+1, H]]
  for i in range(4):
    s, t = pair[i]
    d, max_d = diff[i]
    for j in range(N):
      if S[j] == s: d-=1
      if d <= 0:
        print("NO")
        return
      if T[j] == t: 
        d = min(d+1, max_d)

  print("YES")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()