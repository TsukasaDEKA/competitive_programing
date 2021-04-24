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
        input = """4 4
1 1
4 4
..#.
..#.
.#..
.#.."""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
1 4
4 1
.##.
####
####
.##."""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4
2 2
3 3
....
....
....
...."""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4 5
1 2
4 2
#.###
####.
#..##
#..##"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8 10
5 8
1 1
.#########
##...##.##
##.##.####
##.#######
##......##
##########
#####.###.
#####.####"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  H, W = map(int, input().split(" "))
  Ch, Cw = map(int, input().split(" "))
  wiz_pos = [Ch-1, Cw-1]
  Dh, Dw = map(int, input().split(" "))
  goal_pos = [Dh-1, Dw-1]

  cell_or_wall = []
  count = 0
  for _ in range(H):
    cell_or_wall.append([x == "." for x in list(input())])

  cost_of_cells = [[None] * W for i in range(H)]
  next_cells = set([tuple(wiz_pos)])
  cells_of_wall_side = []

  cost = 0
  
  while len(next_cells) != 0:
    temp_next_cells = set()
    for target_cell in next_cells:
      cost_of_cells[target_cell[0]][target_cell[1]] = cost
      # 周辺の壁じゃないセルを確認する。
      adjacents = [
        [target_cell[0] - 1, target_cell[1]],
        [target_cell[0] + 1, target_cell[1]],
        [target_cell[0], target_cell[1] - 1],
        [target_cell[0], target_cell[1] + 1]
      ]

      for adjacent in adjacents:
        h = adjacent[0]
        w = adjacent[1]
        if h < 0 or h >= H:
          continue
        if w < 0 or w >= W:
          continue

        # print("[h, w] : {}".format([h, w]), "cell_or_wall[h][w] : {}".format(cell_or_wall[h][w]))
        if not cell_or_wall[h][w]:
          # 壁際だった場合は壁際セルリストに追加する。
          if len(cells_of_wall_side) == 0:
            cells_of_wall_side.append(target_cell)
          elif cells_of_wall_side[-1][0] != target_cell[0] or cells_of_wall_side[-1][1] != target_cell[1]:
            cells_of_wall_side.append(target_cell)
          # else: 
          #   print("cells_of_wall_side : {}".format(cells_of_wall_side), "target_cell : {}".format(target_cell))
        elif cost_of_cells[h][w] is None:
          temp_next_cells.add((h, w))
    # print(target_cell)
    # print(temp_next_cells)
    next_cells = temp_next_cells

    if len(next_cells) != 0:
      continue

    # 壁際のセルを確認して、ワープで飛べないか確認する。
    # print(cells_of_wall_side)
    for target_cell in cells_of_wall_side:
      # 飛べるなら next_cells に追加する
      for h in range(target_cell[0] - 2, target_cell[0] + 3):
        if h < 0 or h >= H:
          continue
        for w in range(target_cell[1] - 2, target_cell[1] + 3):
          if w < 0 or w >= W:
            continue
          if cell_or_wall[h][w] and cost_of_cells[h][w] is None:
            next_cells.add((h, w))
    cells_of_wall_side = []
    cost += 1
  
  # for cost_line in cost_of_cells:
  #   print("")
  #   for cell in cost_line:
  #     if cell is None:
  #       print("*", end="")
  #     else:
  #       print(cell, end="")
  # print("")

  if cost_of_cells[goal_pos[0]][goal_pos[1]] is None:
    print(-1)
  else:
    print(cost_of_cells[goal_pos[0]][goal_pos[1]])

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
