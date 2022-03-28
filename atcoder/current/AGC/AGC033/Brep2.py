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
        input = """5 6 11
2 1
RLDRRUDDLRL
URRDRLLDLRD"""
        output = """NO"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """9 3 5
# 1 1
# DDLLR
# RRUUU"""
#         output = """NO"""
#         self.assertIO(input, output)

def resolve():
  # 縦横で分けて考える。
  # 最終的に青木くんがコマを残せるかどうかを判定することを考える。
  # 高橋くんの最後の手が R の時、i の範囲は 1 <= i <= W-1 でなければいけない。
  # 高橋くんの最後の手が L の時、i の範囲は 2 <= i <= W でなければいけない。
  # 青木くんのその前の手が R の時、i の範囲は 
  # これを繰り返していって、範囲の正当性をチェックする。
  H, W, N = map(int, input().split(" "))
  H_, W_ = [int(x)-1 for x in input().split(" ")]
  S = list(input())
  T = list(input())
  T[-1] = ""
  l, r = 0, W-1
  for i in range(N)[::-1]:
    if T[i] == "R": l = max(0, l-1)
    if T[i] == "L": r = min(W-1, r+1)
    if S[i] == "R": r -= 1
    if S[i] == "L": l += 1
    if r < l:
      print("NO")
      return

  if W_ < l or W_ > r:
    print("NO")
    return

  l, r = 0, H-1
  for i in range(N)[::-1]:
    if T[i] == "D": l = max(0, l-1)
    if T[i] == "U": r = min(H-1, r+1)
    if S[i] == "D": r -= 1
    if S[i] == "U": l += 1
    if r < l:
      print("NO")
      return

  if H_ < l or H_ > r:
    print("NO")
    return

  print("YES")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()