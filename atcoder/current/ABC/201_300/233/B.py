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
        input = """3 7
abcdefgh"""
        output = """abgfedch"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 7
reviver"""
        output = """reviver"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 13
merrychristmas"""
        output = """meramtsirhcyrs"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  L, R = [int(x)-1 for x in input().split(" ")]
  S = list(input())
  N = len(S)
  # ans = S[:L]+list(reversed(S[L:R+1]))+S[R+1:]
  ans = [""]*N
  length = R-L+1
  for i in range(N):
    if i < L or R < i:
      ans[i] = S[i]
    else:
      ans[i] = S[R-(i-L)]

  print("".join(ans))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()