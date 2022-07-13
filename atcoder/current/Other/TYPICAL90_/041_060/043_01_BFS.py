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
1 1
3 3
..#
#.#
#.."""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
2 1
2 3
#.#
...
#.#"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 6
2 1
1 5
...#..
.#.##.
.#....
...##."""
        output = """5"""
        self.assertIO(input, output)


def resolve():
  # 方向の変換は 縦->横 or 横->縦 のどちらか以外は意味がない。
  # 縦横で分離して考える？
  # そう考えると Light と似たような処理でいけるかも。
  # 縦・横方向にグルーピング
  # 何個グループを跨いでいけるか考える。
  # それは BFS で行けそう。
  from collections import deque
  H, W = map(int, input().split(" "))
  Sh, Sw = [int(x)-1 for x in input().split(" ")]
  Gh, Gw = [int(x)-1 for x in input().split(" ")]
  MAZE = [[x=="." for x in list(input())] for _ in range(H)]
  # 01 BFS。方向を帰る場合は

  

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
