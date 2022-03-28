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
        input = """2 2 1 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 2 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """40 40 30 30"""
        output = """467620384"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  mod = 998244353
  # B, W >= 1 なので、全ての行、列を埋めるような置き方はできない。
  # 一回条件を満たすように置いて、行と列を自由に並び替えても条件を満たす。
  # 
  N, M, B, W = map(int, input().split(" "))
  N, M = min(N, M), max(N, M)
  B, W = min(B, W), max(B, W)



import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()