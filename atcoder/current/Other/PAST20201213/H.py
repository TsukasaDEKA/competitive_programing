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
1 1
..#
^^.
><."""
        output = """oo#
ooo
xxo"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """10 12
# 9 1
# #.^<..><<...
# #<>.#<^.<<.^
# ^.<>.^.^.^>.
# ^.>#^><#....
# .>.^>#...<<>
# ....^^.#<.<.
# .>^..^#><#.^
# ......#>....
# ..<#<...^>^.
# <..^>^^...^<"""
#         output = """#xxxxxxxxxxx
# #xxx#xxxxxxx
# xooxxxxxxxxx
# xox#xxx#xxxx
# oooxx#xxxxxx
# ooooxxx#xxxx
# ooooox#xx#xx
# oooooo#xxxxx
# ooo#xoooxxxx
# xooxooooooxx"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """15 20
# 13 9
# ####..<#^>#>.<<><^..
# #.>#>.^#^.>><>...^..
# >..<>.#.>.>.>...#..<
# <^>.#..<>^#<#.>.<.^.
# >#<^>.>#^>#^.^.#^><^
# <^.^.#<...<.><#>...#
# .<>....^..#>>#..>>><
# .<#<^#.>#>^^.>.##.^<
# .#.^.....<<#^#><^<<<
# ^.#>.#^.>.^.^<<>..><
# .^#^<^^^<......^>.#^
# .<..#>...^>^.^<..<.^
# #.^.#..#.....>#.^^.>
# .#^..>>><>>>^..#^.^^
# .>#..<..<>.#>..^.#.^"""
#         output = """####xxx#xx#xxxxxxxxx
# #xx#xxx#xxxxxxxxxxxx
# xxxxxx#xxxxxxxxx#xxx
# xxxx#xxxxx#x#xxxxxxx
# x#xxxxx#xx#xxxx#xxxx
# xxoxo#xxxxxxxx#xxxx#
# xxoooooxxx#xx#xxxxxx
# xx#xo#ox#xxxxxx##xxx
# x#xxooooooo#x#xxxxxx
# xx#oo#ooooooxxxoooxx
# xx#ooxoooooooooooo#x
# xxoo#oooooooooooooox
# #ooo#oo#ooooox#oooox
# x#oooxxxxoooooo#ooox
# xx#oooooooo#oooxo#ox"""
#         self.assertIO(input, output)


def resolve():
  from collections import deque
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  # r, c から幅優先探索で逆走していって、到達できるとことなら o、そうでないなら x
  H, W = map(int, input().split(" "))
  r, c = map(int, input().split(" "))
  S = [list(input()) for _ in range(H)]
  ans = [["x"]*W for _ in range(H)]

  for h in range(H):
    for w in range(W):
      if S[h][w] =="#": ans[h][w]="#"
  
  next_grids = deque([(r, c)])
  ans[r][c] = "o"
  while next_grids:
    x, y = next_grids.popleft()
    for i in range(4):
      n_x = x + dx[i]
      n_y = y + dy[i]
      if n_x>=0 and n_y>=0 and n_x<H and n_y<W:
        if ans[n_x][n_y] != "o":
          # このマス(x, y)に来れない条件を書く
          # . # < ^ > v 
          if S[n_x][n_y]=="#": continue
          # x, y より上方向で、 . か v じゃない
          if dx[i]==-1 and dy[i]==0 and (S[n_x][n_y]!="." and S[n_x][n_y]!="v"): continue
          # x, y より下方向で、 . か ^ じゃない
          if dx[i]==1 and dy[i]==0 and (S[n_x][n_y]!="." and S[n_x][n_y]!="^"): continue
          # x, y より左方向で、 . か > じゃない
          if dx[i]==0 and dy[i]==-1 and (S[n_x][n_y]!="." and S[n_x][n_y]!=">"): continue
          # x, y より右方向で、 . か < じゃない
          if dx[i]==0 and dy[i]==1 and (S[n_x][n_y]!="." and S[n_x][n_y]!="<"): continue
          ans[n_x][n_y] = "o"
          next_grids.append((n_x, n_y))
  for a in ans:
    print(*a, sep="")
# resolve()

if __name__ == "__main__":
    unittest.main()
