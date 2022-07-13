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
())"""
        output = """(())"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
)))())"""
        output = """(((()))())"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
))))(((("""
        output = """(((())))(((())))"""
        self.assertIO(input, output)

def resolve():
  # ( はできるだけ左に入れて ) はできるだけ右に入れる。
  # 既にペアになっている組み合わせの間に挿入する必要はなさそう。
  # なんかキューを使いそう。
  # ( を見た時に +1 する。
  # ) を見た時に値が 0 であれば左端に ( を足す。
  # ) を見た時に値が 0 でなければその値を -1 する。
  # 最後にカウントした分の ( を末尾に足す。
  inf = 10**18+1
  N = int(input())
  S = list(input())
  l = 0
  r = 0

  for i in range(N):
    if S[i] == "(":
      r += 1
    else:
      if r == 0: l += 1
      else: r -= 1

  print("("*l + "".join(S) + ")"*r)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()