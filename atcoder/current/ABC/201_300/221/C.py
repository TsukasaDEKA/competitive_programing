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
        input = """123"""
        output = """63"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1010"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """998244353"""
        output = """939337176"""
        self.assertIO(input, output)

def resolve():
  from itertools import permutations

  inf = 10**18+1
  S = sorted(list(input()), reverse=True)
  N = len(S)

  ans = 0
  for bit in range(1, 1<<N-1):
    a = []
    b = []
    for i in range(N):
      if bit&(1<<i):
        a.append(S[i])
      else:
        b.append(S[i])
    a = int("".join(a))
    b = int("".join(b))
    # print(a, b)
    ans = max(ans, a*b)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()