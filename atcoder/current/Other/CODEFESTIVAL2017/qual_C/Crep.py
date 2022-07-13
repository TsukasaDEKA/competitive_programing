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
        input = """xabxa"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """ab"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """a"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """oxxx"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 前後から探索して行って、矛盾が出ないかチェックする。
  S = list(input())
  N = len(S)
  l, r = 0, N-1

  ans = 0
  while l < r:
    if S[l] != S[r]:
      if S[l] == "x":
        while S[l]  == "x":
          ans += 1
          l += 1
      else:
        while S[r]  == "x":
          ans += 1
          r -= 1

    if S[l] != S[r]:
      print(-1)
      return

    l += 1
    r -= 1
  else:
    print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()