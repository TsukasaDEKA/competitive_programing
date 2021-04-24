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
        input = """3
1 2 3 4 5 6"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 4 5 8 7 6 3 2"""
        output = """20"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1 1 10 6 7 9 1 1"""
        output = """21"""
        self.assertIO(input, output)

def resolve():
  # 1 6 2 5 3 4 みたいな 状態を考える。
  # 愚直に大きい方から取っていくと 6 を取った後に青木くんに 5 を取られる。
  # 5 を先に取って、2 を取らせて、6 を取って、3 を取らせて、 4 をとるといった風にする必要がある。
  # 青木くんにより小さい数字を取らせる方法を考える。
  # 高橋くんが真ん中より左側を取ると青木くんは次に真ん中から右側を取る。
  # 高橋くんが真ん中より右側を取ると青木くんは次に真ん中から左側を取る。
  # 1 4 5 8 7 6 3 2 => 8
  # 1 4 5 6 3 2 => 6
  # 1 4 3 2 => 4
  # 1 2 => 2
  # 合計 20
  # 大きい方を急いで取る必要は無い。
  # 10 3 5 8 6 9 => 9
  # 10 3 8 6 => 8
  # 10 6 => 10
  # 10 3 5 8 6 9 => 8
  # 10 3 6 9 => 6
  # 10 9 => 10
  # 10 7 8 5 6 9 => 9, 8, 10
  # 大きい方から N 個順に取れる？
  # 取れない組み合わせが存在するっぽい。
  # 10 6 8 5 7 9 => 9, 8, 10
  # 10 6 1 1 1 1 7 9 => 10 6 7 9 を取れる。
  # 1 1 10 6 7 9 1 1 => 10 9 1 1 を取れる。
  # 中心からより遠い方と入れ替えることができる。
  # 10 3 5 8 6 9 => 9 3 5 8 6 10 => [5 3 9][8 6 10]
  # ヒープ使ってやってみる。
  from heapq import heappop, heappush

  N = int(input())
  V = [int(x) for x in input().split(" ")]
  V_l = V[N-1::-1]
  V_r = V[N:]
  # V_l  = [(v, i) for i, v in enumerate(reversed(V[:N]))]
  # V_r = [(v, i) for i, v in enumerate(V[N:])]

  ans = []
  for i in range(N):
    min_, max_ = min(V_l[i], V_r[i]), max(V_l[i], V_r[i])
    heappush(ans, max_)
    if ans[0] < min_:
      _ = heappop(ans)
      heappush(ans, min_)

  print(sum(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
