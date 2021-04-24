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
...
.#.
..."""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 6
..#..#
......
#..#..
......
.#....
....#."""
        output = """3"""
        self.assertIO(input, output)

from collections import deque

def resolve():
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  # 幅優先探索をして各マスを何手目で塗ったかを記録していって、手の数の最大値をとる。
  inf = 10**7+1
  H, W = map(int, input().split(" "))
  A = [[inf if x=="." else 0 for x in list(input())] for _ in range(H)]
  next_grids = deque()

  # 幅優先探索を初めから黒いマスから始めるので、黒マスを探す。O(HW) だけど計算軽いしいけそう。
  for h in range(H):
    for w in range(W):
      if A[h][w]==0: next_grids.append((h, w))

  ans = 0
  while next_grids:
    h, w = next_grids.popleft()
    for i in range(4):
      h_ = h + dx[i]
      w_ = w + dy[i]
      if h_>=0 and w_>=0 and h_<H and w_<W and A[h_][w_]==inf:
        A[h_][w_]=A[h][w]+1
        next_grids.append((h_, w_))
        ans=max(ans, A[h_][w_])
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
