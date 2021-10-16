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
        input = """aab 2"""
        output = """aba"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """baba 4"""
        output = """baab"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """ydxwacbz 40320"""
        output = """zyxwdcba"""
        self.assertIO(input, output)

def resolve():
  from itertools import permutations

  # 8! 個
  S, K = input().split(" ")
  K = int(K)
  S = list(S)
  ans = set()
  for p in permutations(S, len(S)):
    ans.add("".join(p))

  ans = sorted(list(ans))
  print(ans[K-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()