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
        input = """1234"""
        output = """1736"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31415926535897932384626433832795"""
        output = """85607943"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  mag = 1
  S = [int(x) for x in list(input())][::-1]
  N = len(S)
  ans = 0
  for i in range(N):
    ans+=(pow(2, (N-1-i), mod)*S[i]*mag)%mod
    if ans >= mod: ans%=mod
    mag*=10
    mag+=pow(2, i, mod)
    if mag >= mod: mag%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()