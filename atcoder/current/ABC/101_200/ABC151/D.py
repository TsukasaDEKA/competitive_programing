import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff= None
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
...
..."""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5
...#.
.#.#.
.#..."""
        output = """10"""
        self.assertIO(input, output)

from collections import deque
 
def resolve():
  inf = 10**10+1
  H, W = map(int, input().split(" "))
  maze = [[x=="." for x in list(input())] for _ in range(H)]
  # H, W <= 20 なので、全ての点を Start にして幅優先探索を行っても 20*20*20 = 8000 以下になるので計算量的には間に合う。
  
  ans = 0
  for h in range(H):
    for w in range(W):
      if not maze[h][w]: continue
      step_map = [[inf]*W for _ in range(H)]
      next_nodes = deque([(h, w)])
      while next_nodes:
        h_c, w_c =  next_nodes.popleft()
        if step_map[h_c][w_c] != inf: continue
        adjacents = inf
        if h_c > 0  : adjacents = min(adjacents, step_map[h_c-1][w_c])
        if h_c < H-1: adjacents = min(adjacents, step_map[h_c+1][w_c])
        if w_c > 0  : adjacents = min(adjacents, step_map[h_c][w_c-1])
        if w_c < W-1: adjacents = min(adjacents, step_map[h_c][w_c+1])
        if adjacents != inf: step_map[h_c][w_c] = adjacents+1
        else: step_map[h_c][w_c] = 0
        ans = max(ans, step_map[h_c][w_c])
 
        if h_c > 0:
          if maze[h_c-1][w_c] and step_map[h_c-1][w_c] == inf:
            next_nodes.append((h_c-1,w_c))
        if h_c < H-1:
          if maze[h_c+1][w_c] and step_map[h_c+1][w_c] == inf:
            next_nodes.append((h_c+1,w_c))
        if w_c > 0  :
          if maze[h_c][w_c-1] and step_map[h_c][w_c-1] == inf:
            next_nodes.append((h_c,w_c-1))
        if w_c < W-1:
          if maze[h_c][w_c+1] and step_map[h_c][w_c+1] == inf:
            next_nodes.append((h_c,w_c+1))
 
  print(ans)
 
resolve()

if __name__ == "__main__":
    unittest.main()
