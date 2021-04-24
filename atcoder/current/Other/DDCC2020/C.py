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
        input = """3 3 5
#.#
.#.
#.#"""
        output = """1 2 2
1 3 4
5 5 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 7 7
#...#.#
..#...#
.#..#.."""
        output = """1 1 1 1 2 2 3
4 4 4 4 2 2 5
6 6 6 6 7 7 5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """13 21 106
.....................
.####.####.####.####.
..#.#..#.#.#....#....
..#.#..#.#.#....#....
..#.#..#.#.#....#....
.####.####.####.####.
.....................
.####.####.####.####.
....#.#..#....#.#..#.
.####.#..#.####.#..#.
.#....#..#.#....#..#.
.####.####.####.####.
....................."""
        output = """12 12 23 34 45 45 60 71 82 93 93 2 13 24 35 35 17 28 39 50 50
12 12 23 34 45 45 60 71 82 93 93 2 13 24 35 35 17 28 39 50 50
12 12 56 89 89 89 60 104 82 31 31 46 13 24 35 35 61 61 39 50 50
12 12 67 67 100 100 60 9 9 42 42 57 13 24 6 72 72 72 72 72 72
12 12 78 5 5 5 20 20 20 53 68 68 90 24 6 83 83 83 83 83 83
16 16 27 38 49 49 64 75 86 97 79 79 90 101 6 94 94 105 10 21 21
16 16 27 38 49 49 64 75 86 97 79 79 90 101 6 94 94 105 10 21 21
32 32 43 54 65 65 80 11 106 95 22 22 33 44 55 55 70 1 96 85 85
32 32 43 54 76 76 91 11 106 84 84 4 99 66 66 66 81 1 96 74 74
14 14 3 98 87 87 102 11 73 73 73 4 99 88 77 77 92 92 63 63 63
25 25 3 98 87 87 7 29 62 62 62 15 99 88 77 77 103 19 30 52 52
36 36 47 58 69 69 18 29 40 51 51 26 37 48 59 59 8 19 30 41 41
36 36 47 58 69 69 18 29 40 51 51 26 37 48 59 59 8 19 30 41 41"""
        self.assertIO(input, output)


def resolve():
  # 積分画像作って全探索？ 全探索コスト + 塗りコスト + 積分画像作成コストで 3*300*300 なので間に合う？
  # 探索コストがもうちょいかかるかも。間に合うか微妙
  H, W, K = map(int, input().split(" "))
  cake = [[x=="#" for x in list(input())] for _ in range(H)]
  i_sb = [[0]*(W+1) for _ in range(H+1)]
  for h in range(1, H+1):
    for w in range(1, W+1):
      i_sb[h][w] = cake[h-1][w-1] + i_sb[h-1][w] + i_sb[h][w-1] - i_sb[h-1][w-1]

  ans = [[0]*W for _ in range(H)]
  cake_no = 1
  # 探索。塗り潰しは内部で行う。
  for h in range(H):
    for w in range(W):
      # 塗り済みならばスキップ
      if ans[h][w]: continue
      end_h = h
      end_w = w
      # いちごの個数が 2 になる直前まで水平方向に進めてく (塗ってあってもやめる)
      if end_w < W-1:
        while i_sb[end_h+1][end_w+2] - i_sb[h][end_w+2] - i_sb[end_h+1][w] + i_sb[h][w] <= 1 and ans[end_h][end_w+1] == 0:
          end_w += 1
          if end_w >= W-1: break

      # いちごの個数が 2 以上になる直前まで垂直方向に進めてく (塗ってあってもやめるが、多分塗ってあるケースは無い)
      if end_h < H-1:
        while i_sb[end_h+2][end_w+1] - i_sb[h][end_w+1] - i_sb[end_h+2][w] + i_sb[h][w] <= 1 and ans[end_h+1][end_w] == 0:
          end_h += 1
          if end_h >= H-1: break

      # ここで苺の個数が 0 の場合、垂直方向に 1 個進めてから苺の個数が 1 個になるまで戻す。
      # そのあと、いちごの個数が 2 以上になる直前まで垂直方向に進めてく
      # ここがコストかかりそうだけど 300*300 なので間に合う・・・と思う
      if i_sb[end_h+1][end_w+1] - i_sb[h][end_w+1] - i_sb[end_h+1][w] + i_sb[h][w] == 0:
        end_h+=1
        while i_sb[end_h+1][end_w] - i_sb[h][end_w] - i_sb[end_h+1][w] + i_sb[h][w] >= 1:
          end_w-=1

        if end_h <= H-1:
          while i_sb[end_h+2][end_w+1] - i_sb[h][end_w+1] - i_sb[end_h+2][w] + i_sb[h][w] == 1:
            end_h += 1
            if end_h >= H-1: break
        # print()
        # print(end_h, end_w)
      # 塗る
      for c_h in range(h, end_h+1):
        for c_w in range(w, end_w+1):
          ans[c_h][c_w] = cake_no

      # for a in ans:
      #   print(*a)
      # print()

      cake_no += 1

  for a in ans:
    print(*a)

resolve()


if __name__ == "__main__":
    unittest.main()
