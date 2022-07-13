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
        input = """2 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 123456789"""
        output = """205695670"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  # N がとても大きい。DP だと間に合わない。
  # A に二進数で表した時の桁数が同じものが 2 個含まれる場合のことを考える。
  # それぞれのインデックスを i, j (i < j) とした時。
  # Bi > Bj となるので、これは条件を満たさない。
  # つまり、「A に二進数で表した時の桁数が同じものが 2 個以上含まれない」ということになる。
  # つまり、 (1<<N)-1 > M の時、答えは 0
  # そう考えると M < 2^60 なので、N は 60 未満
  # これなら DP でも間に合う。
  
  N, M = map(int, input().split(" "))
  if (1<<(N-1)) > M:
    print(0)
    return

  # 初手
  pattern = M - 1<<M.bit_length()



  for m in range(1<<())
  print(hoge)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()