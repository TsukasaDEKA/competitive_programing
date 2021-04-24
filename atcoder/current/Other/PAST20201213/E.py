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

#     def test_Sample_Input_1(self):
#         input = """3 3
# ...
# .#.
# ..#
# #.#
# ###
# ..."""
#         output = """Yes"""
#         self.assertIO(input, output)
    def test_Sample_Input_1(self):
        input = """3 3
...
.#.
..#
#.#
###
..."""
        output = """Yes"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """3 3
# ...
# #..
# #.#
# .#.
# .##
# ##."""
#         output = """No"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """2 5
# .....
# ..#..
# ..##.
# .###."""
#         output = """Yes"""
#         self.assertIO(input, output)

def resolve():
  # 10*10 なので全探索？
  inf = 10**10+1
  H, W = map(int, input().split(" "))
  S = [list(input()) for _ in range(H)]
  T = [list(input()) for _ in range(H)]

  # T の最小 x, y と最大 x, y を出す。
  min_x = min_y = inf
  max_x = max_y = 0
  for h in range(H):
    for w in range(W):
      if T[h][w] == "#":
        min_x = min(min_x, h)
        min_y = min(min_y, w)
        max_x = max(max_x, h)
        max_y = max(max_x, w)

  Tx_range = max_x-min_x+1
  Ty_range = max_y-min_y+1

  # print(max_x, min_x)
  # print(max_y, min_y)
  # print(Tx_range, Ty_range)
  for h in range(H-Tx_range+1):
    for w in range(W-Ty_range+1):
      # h, w は開始点
      can_put = True
      for x in range(Tx_range):
        for y in range(Ty_range):
          if T[min_x+x][min_y+y] == "#" and S[h+x][w+y]== "#":
            can_put = False
            break
        if not can_put: break
      if can_put:
        print("Yes")
        return

  # 90°回転
  for h in range(H-Tx_range+1):
    for w in range(W-Ty_range+1):
      # h, w は開始点
      can_put = True
      for x in range(Tx_range):
        for y in range(Ty_range):
          if T[min_x+x][min_y+y] == "#" and S[h+x][w+y]== "#":
            can_put = False
            break
        if not can_put: break
      if can_put:
        print("Yes")
        return
  print("No")

# resolve()

if __name__ == "__main__":
    unittest.main()
