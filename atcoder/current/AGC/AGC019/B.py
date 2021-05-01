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
        input = """aatt"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """xxxxxxxxxx"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """abracadabra"""
        output = """44"""
        self.assertIO(input, output)

def resolve():
  # 操作は一回まで
  # 組み合わせ数は N*(N-1)/2 個あるので、愚直だと厳しい
  # 一旦反転して、LCS かける？(それでどうなるのって感じだけど。)
  # N <= 2*10**5 は N**2 だと厳しいけど NlogN とか 多少の定数倍は通りそう。
  A = list(input())
  revA = reversed(A)
  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
