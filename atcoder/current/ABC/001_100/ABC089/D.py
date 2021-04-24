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
        input = """3 3 2
1 4 3
2 5 7
8 9 6
1
4 8"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 2 3
3 7
1 4
5 2
6 8
2
2 2
2 2"""
        output = """0
0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5 4
13 25 7 15 17
16 22 20 2 9
14 11 12 1 19
10 6 23 8 18
3 21 5 24 4
3
13 13
2 10
13 13"""
        output = """0
5
0"""
        self.assertIO(input, output)

def resolve():
  # 毎回指定される座標を検索していたら大変なので、数値が決まったら O(1) で座標をとってこれるようにする。
  # TLE をしたので対策を考える。
  # クエリが多いので、最初に i -> j を全て計算してみる。 i から開始して、i+kD 毎に i => i+kD に移動するまでのコストの総和を出していく。
  # O(H*W) で構築できて、クエリに対して O(1) で回答できる。
  H, W, D = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]
  map_A = [None]*(H*W+1)
  for h in range(H):
    for w in range(W):
      map_A[A[h][w]] = (h, w)

  costs = [0]*(H*W+1)
  for start in range(1, H*W+1):
    if costs[start]: continue
    recent_h, recent_w = map_A[start]
    mp = 0
    for tar in range(start+D, H*W+1, D):
      current_h, current_w = map_A[tar]
      mp += abs(recent_h - current_h) + abs(recent_w - current_w)
      costs[tar] = mp
      recent_h, recent_w = current_h, current_w

  Q = int(input())
  for _ in range(Q):
    L, R = map(int, input().split(" "))
    print(costs[R] - costs[L])
resolve()

if __name__ == "__main__":
    unittest.main()
