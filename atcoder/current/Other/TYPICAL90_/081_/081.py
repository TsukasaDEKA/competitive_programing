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
        input = """3 4
1 1
2 5
7 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 123
4 5
678 901"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 10
20 20
20 20
20 30
20 40
30 20
30 30
40 20"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # チェビシェフ距離でソートしたい。
  # 原点からのチェビシェフ距離を求めてソートする？
  # 5000*5000 のフィールドで、大きさ K の正方形をおいた時に、
  # その内側に含まれる点が最大になる座標を求める。
  # 二次元累積和を使えば正方形内部の点は O(1) で求められる。
  # フィールドサイズが 5000*5000 なので、
  # 最大 25000000 回の計算なのでギリギリ間に合うか。
  N, K = map(int, input().split(" "))
  FIELD_SIZE = 5000
  FIELD = [[0]*FIELD_SIZE for _ in range(FIELD_SIZE)]
  for i in range(N):
    a, b = [int(x)-1 for x in input().split(" ")]
    FIELD[a][b]+=1

  # 二次元累積和を作る。
  INTE_FIELD = [[0]*(FIELD_SIZE+1) for _ in range(FIELD_SIZE+1)]
  for h in range(FIELD_SIZE):
    INTE_FIELD_h = INTE_FIELD[h]
    INTE_FIELD_h_1 = INTE_FIELD[h+1]
    FIELD_h = FIELD[h]
    for w in range(FIELD_SIZE):
      INTE_FIELD_h_1[w+1] = FIELD_h[w]+INTE_FIELD_h_1[w]+INTE_FIELD_h[w+1]-INTE_FIELD_h[w]

  # サイズ K の区間における最大値を求める。
  ans = 0
  d = K+1
  for h in range(FIELD_SIZE-K):
    INTE_FIELD_h = INTE_FIELD[h]
    INTE_FIELD_h_d = INTE_FIELD[h+d]
    for w in range(FIELD_SIZE-K):
      temp = INTE_FIELD_h_d[w+d]-INTE_FIELD_h_d[w]-INTE_FIELD_h[w+d]+INTE_FIELD_h[w]
      if ans < temp: ans = temp
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()