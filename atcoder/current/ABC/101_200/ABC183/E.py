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
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
...#
....
..#.
...."""
        output = """84"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 10
..........
..........
..........
..........
..........
..........
..........
.........."""
        output = """13701937"""
        self.assertIO(input, output)

def resolve():
  # さっぱりわからん。
  # 例1では (1, 2) で一旦止まった場合、移動方法は 3 通りある。
  # 深さ優先探索していくか？
  # 移動方法の数が 10**9+7 を超える可能性があるので到底間に合わない。
  # 再帰的に解いたらどうだろう。
  # ゴール (H, W) に次の一手で到達できるマスが X0 個あって、
  # それぞれのマスに次の一手で到達できるマスが X1 個あって・・・
  # と考えていくといけそう？
  # ゴール (H, W) から逆順で考えていくといけそう。
  # 計算量を減らす方法を考えなきゃ。
  # とりあえず愚直な実装をしてみて様子をみる。
  # TLE したので 累積和を考える。
  # 縦方向の累積和、横方向の累積和、斜めの累積和をそれぞれ作る。

  mod = 10**9+7
  H, W = map(int, input().split(" "))
  S = [list(input()) for _ in range(H)]

  # 縦横斜めの累積和
  row = [[0]*W for _ in range(H)]
  column = [[0]*W for _ in range(H)]
  diag = [[0]*W for _ in range(H)]
  row[-1][-1] = column[-1][-1] = diag[-1][-1] = 1

  for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
      if h == H-1 and w == W-1: continue
      if S[h][w] == "#": continue

      val = 0
      if w+1 < W: val += row[h][w+1]
      if h+1 < H: val += column[h+1][w]
      if h+1 < H and w+1 < W: val += diag[h+1][w+1]

      row[h][w] = val
      if w+1 < W:
        row[h][w] += row[h][w+1]
        if row[h][w] >= mod: row[h][w]%=mod

      column[h][w] = val
      if h+1 < H:
        column[h][w] += column[h+1][w]
        if column[h][w] >= mod: column[h][w]%=mod

      diag[h][w] = val
      if h+1 < H and w+1 < W:
        diag[h][w] += diag[h+1][w+1]
        if diag[h][w] >= mod: diag[h][w]%=mod

  print((row[0][1]+column[1][0]+diag[1][1])%mod)
# resolve()

if __name__ == "__main__":
  unittest.main()
