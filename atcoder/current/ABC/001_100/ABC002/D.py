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
        input = """5 3
1 2
2 3
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_1(self):
        input = """3 1
1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3
1 2
2 3
3 4"""
        output = """2"""
        self.assertIO(input, output)


    def test_Sample_Input_3(self):
        input = """7 9
1 2
1 3
2 3
4 5
4 6
4 7
5 6
5 7
6 7"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """12 0"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
  # 全探索で間に合うか？
  # 選び方は 2**12 通りある。
  # bit DP か。
  # dp[U] = 議員集合 U を選んだ時の最大の派閥に属する議員数
  N, M = map(int, input().split(" "))
  connections = [[0]*N for _ in range(N)]
  for _ in range(M):
    x, y = [int(x)-1 for x in input().split(" ")]
    connections[x][y] = 1
    connections[y][x] = 1
  
  dp = [0]*(1<<N)
  for u in range(1<<N):
    for i in range(N):
      if u&(1<<i):
        for j in range(N):
          if i==j: continue
          if u&(1<<j) and connections[i][j] == 0:
            break
        else:
          dp[u] = max(dp[u], dp[u-(1<<i)]+1)

  print(max(dp))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()