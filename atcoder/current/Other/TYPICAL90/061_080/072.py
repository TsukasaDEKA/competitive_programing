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

    def test_入力例_1(self):
        input = """3 3
...
.#.
..."""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 6
......"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4
....
#...
....
...#"""
        output = """12"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  from collections import deque
  popcnt = lambda x: bin(x).count("1")
  # 最大の閉路を求める。
  # 升目の数は高々 16 なので、通ったマスの状態を bit で受け渡しながら DFS を行う。
  # スタート地点にたどり着いた時点で立ってるビットの数を数える。
  H, W = map(int, input().split(" "))
  C = [[1 if x == "." else 0 for x  in list(input())] for _ in range(H)]

  # 初動 -1 にしておくと条件を満たす経路が見つからなかった時の処理が楽
  ans = -1
  nexts = deque()
  # sh, sw はスタート地点の座標。
  # 全マスにおいて、そこからスタートした場合の最大経路を求める。
  for sh in range(H):
    for sw in range(W):
      # 開始地点が山だったら計算スキップ
      if C[sh][sw] == 0: continue

      # 開始地点に辿り着いた時に判定！ってのをしたいので、開始地点の隣接マスからスタートさせる。
      for i in range(4):
        h_ = sh+dh[i]
        w_ = sw+dw[i]
        if h_ >= 0 and h_ < H and w_ >= 0 and w_ < W:
          if C[h_][w_]: nexts.append((h_, w_, 1<<(h_*W+w_+1)))

      # start_bit : 開始地点座標の bit 表現。
      start_bit = 1<<(sh*W+sw+1)
      while nexts:
        # h, w, bit = h, w 座標 と今まで訪れた地点の bit 表現
        h, w, bit = nexts.pop()
        if bit&start_bit:
          # popcnt(bit) : 訪れたことがあるマスの数を数えてる。
          if popcnt(bit) >= 3:
            ans = max(ans, popcnt(bit))
          continue
        
        for i in range(4):
          h_ = h+dh[i]
          w_ = w+dw[i]
          if h_ >= 0 and h_ < H and w_ >= 0 and w_ < W:
            # 今まで訪れたことがなければ探索先に追加する。
            if C[h_][w_] and not bit&(1<<(h_*W+w_+1)):
              nexts.append((h_, w_, bit+(1<<(h_*W+w_+1))))

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
