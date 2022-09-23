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
        input = """5
1
2
1
2
2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
4
2
5
4
2
4"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
1
3
1
2
3
3
2"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # 解説 AC
  # https://betrue12.hateblo.jp/entry/2019/03/17/011847
  # 解説を読んでも理解できないので、一度実装してみる。
  mod = 10**9+7
  N = int(input())
  C = [int(input()) for _ in range(N)]
  DP = [1]*N
  last_index_of_c = defaultdict(int)
  last_index_of_c[C[0]] = 0
  for i in range(1, N):
    if C[i] not in last_index_of_c or C[i] == C[i-1]:
      DP[i] = DP[i-1]
    else:
      DP[i] = DP[i-1]+DP[last_index_of_c[C[i]]]

    last_index_of_c[C[i]] = i
    if DP[i] >= mod: DP[i]%=mod

  print(DP[-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
