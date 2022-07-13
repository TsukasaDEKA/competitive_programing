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
        input = """3
PEEL
AAAAAAAAAA
CODEJAMDAY"""
        output = """Case #1: PEEEEL
Case #2: AAAAAAAAAA
Case #3: CCODDEEJAAMDAAY"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())


  for t in range(1, T+1):
    S = list(input())
    N = len(S)
    ans = ""
    count = 0
    for i in range(N-1):
      count += 1
      if S[i] < S[i+1]:
        ans += S[i]*(2*count)
        count = 0
      elif S[i] > S[i+1]:
        ans += S[i]*count
        count = 0
    ans += S[N-1]*count
    ans += S[-1]
    print("Case #{0}: {1}".format(t, ans))

resolve()

if __name__ == "__main__":
  unittest.main()