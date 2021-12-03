import sys
from io import StringIO
from typing import Pattern
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
        input = """2 2 2"""
        output = """16"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 14 15926535"""
        output = """109718301"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  N, K, M = map(int, input().split(" "))
  if M%mod == 0:
    print(0)
    return
  pattern = pow(K, N, mod-1)
  ans = pow(M, pattern, mod)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()