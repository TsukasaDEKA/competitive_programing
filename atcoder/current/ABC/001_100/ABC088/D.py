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
..#
#..
..."""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 37
.....................................
...#...####...####..###...###...###..
..#.#..#...#.##....#...#.#...#.#...#.
..#.#..#...#.#.....#...#.#...#.#...#.
.#...#.#..##.#.....#...#.#.###.#.###.
.#####.####..#.....#...#..##....##...
.#...#.#...#.#.....#...#.#...#.#...#.
.#...#.#...#.##....#...#.#...#.#...#.
.#...#.####...####..###...###...###..
....................................."""
        output = """209"""
        self.assertIO(input, output)

#     def test_Sample_Input_1(self):
#         input = """3 3
# ..#..#..#..#
# ..#..#..#..#
# ..#..#..#..."""
#         output = """2"""
#         self.assertIO(input, output)


from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def resolve():
  # H*W-壁の個数-最短経路のマスの数。
  # 壁を数えて、幅優先探索で最短経路でのステップ数を数えて、最後に計算する。
  # O(50*50)程度なので大丈夫
  inf = 10**3+1
  H, W = map(int, input().split(" "))
  maze = [[x=="." for x in list(input())] for _ in range(H)]
  is_visited = [[False]*W for _ in range(H)]
  is_visited[0][0] = True
  step_count = [[inf]*W for _ in range(H)]
  step_count[0][0] = 1

  next_grids = deque([(0, 0)])
  while next_grids:
    x, y = next_grids.popleft()
    for i in range(4):
      n_x = x + dx[i]
      n_y = y + dy[i]
      if n_x>=0 and n_y>=0 and n_x<H and n_y<W:
        if not is_visited[n_x][n_y] and maze[n_x][n_y]:
          is_visited[n_x][n_y] = True
          step_count[n_x][n_y] = step_count[x][y]+1
          next_grids.append((n_x, n_y))

  # print(*step_count, sep="\n")
  if step_count[H-1][W-1] == inf:
    print(-1)
    return

  wall_count=0
  for h in range(H):
    for w in range(W):
      if not maze[h][w]: wall_count+=1
  print(H*W-wall_count-step_count[H-1][W-1])

resolve()

if __name__ == "__main__":
    unittest.main()
