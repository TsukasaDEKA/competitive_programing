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
        input = """2 2
B.
.R"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
R.R
BBR
..."""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 2
BB
BB"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  mod = 998244353
  from collections import defaultdict

  # 右上から左上にいくときに同じでなければいけない。
  # 斜めに見ていって、全て . なら 2、一種類だけなら 1 、そうでない場合は 0 をかける。
  H, W = map(int, input().split(" "))
  S = [[x for x in list(input())] for _ in range(H)]
  ans = 1
  for i in range(H+W-1):
    count = defaultdict(int)
    for j in range(min(i+1, W)):
      if i-j < 0 or i-j >= H or j >= W: continue
      # print(S[i-j][j])
      count[S[i-j][j]]+=1

    if count["R"] >= 1 and count["B"] >= 1:
      print(0)
      return
    if count["R"] == 0 and count["B"] == 0:
      ans *= 2
      

  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
