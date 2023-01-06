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
        input = """3 3
.#.
..#
#.."""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 4
....
...."""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 3
###
###
...
###"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  # H*W <= 160,000なので、O(N)くらいじゃないとキツそう。
  # 経路は問わず、あくまで 黒と白のペア
  # 実はそれぞれが交流のない(移動できない)島に分割できることがわかる。
  # 幅優先探索で島ごとの黒と白のマスの数をそれぞれ数えて、
  # 黒の個数 * 白の個数 を島ごとに足していく。
  from collections import deque
  H, W = map(int, input().split(" "))
  S = [list(input()) for _ in range(H)]
  checked = [[False]*W for _ in range(H)]

  nexts = deque()
  ans = 0
  for h in range(H):
    for w in range(W):
      if checked[h][w]: continue
      # ここから幅優先探索
      nexts.append((h, w))
      checked[h][w] = True
      black = 0
      white = 0
      while nexts:
        h_n, w_n = nexts.popleft()
        if S[h_n][w_n] == "#": black += 1
        else: white += 1

        for i in range(4):
          h_n_ = h_n + dh[i]
          w_n_ = w_n + dw[i]
          if h_n_ >= 0 and h_n_ < H and w_n_ >= 0 and w_n_ < W:
            if S[h_n][w_n] != S[h_n_][w_n_]:
              if checked[h_n_][w_n_]: continue
              checked[h_n_][w_n_] = True
              nexts.append((h_n_, w_n_))
      ans += black*white

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
