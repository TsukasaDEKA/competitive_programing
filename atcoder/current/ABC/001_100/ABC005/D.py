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
        input = """3
3 2 1
2 2 1
1 1 1
3
1
4
9"""
        output = """3
9
14"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 1 1
1 1 1
9 9 9
1
4"""
        output = """27"""
        self.assertIO(input, output)


def resolve():
  # 一旦累積和をとって、全ての部分における美味しさの合計値を求める。
  # table[i] := i 個以下のたこ焼きを作った時の最大値とし、table[P] が答え。
  N = int(input())
  D = [[int(x) for x in input().split(" ")] for _ in range(N)]
  sumD = [[0]*(N+1) for _ in range(N+1)]
  for h in range(N):
    for w in range(N):
      sumD[h+1][w+1] = D[h][w]+sumD[h][w+1]+sumD[h+1][w]-sumD[h][w]

  table = [0]*(N**2+1)
  for h1 in range(N):
    for w1 in range(N):
      for h2 in range(h1+1, N+1):
        for w2 in range(w1+1, N+1):
          val = sumD[h2][w2]+sumD[h1][w1]-sumD[h2][w1]-sumD[h1][w2]
          if val > table[(h2-h1)*(w2-w1)]:
            table[(h2-h1)*(w2-w1)] = val

  for i in range(1, N**2+1):
    table[i] = max(table[i-1], table[i])

  Q = int(input())
  for _ in range(Q):
    P = int(input())
    print(table[P])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()