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
        input = """16"""
        output = """73"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """238"""
        output = """13870"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """999999999999999999"""
        output = """762062362"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  N = int(input())
  ans = 0
  for i in range(1, 19):
    K = max(0, min((10**i)-1, N)-10**(i-1)+1)
    if K == 0:
      break
    ans += (K*(K+1)//2)%mod
    if ans >= mod: ans%=mod

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()