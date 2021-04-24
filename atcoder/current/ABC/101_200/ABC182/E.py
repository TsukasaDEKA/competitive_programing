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
        input = """3 3 2 1
1 1
2 3
2 2"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4 3 3
1 2
1 3
3 4
2 3
2 4
3 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5 5 1
1 1
2 2
3 3
4 4
5 5
4 2"""
        output = """24"""
        self.assertIO(input, output)

def resolve():
  # 近い問題を解いたことがある。
  # 右方向にチェック、左方向にチェック、下方向にチェック、上方向にチェックを繰り返して、ライトに照らされているかどうかを確認する。
  # 9000000 <= 10**7 なので Python だとちょっと厳しいかも。
  H, W, N, M = map(int, input().split(" "))
  lights = [[int(x)-1 for x in input().split(" ")] for _ in range(N)]
  grid = [["."]*W for _ in range(H)]
  ans_map_row = [[False]*W for _ in range(H)]
  ans_map_column = [[False]*W for _ in range(H)]

  for _ in range(M):
    h, w = [int(x)-1 for x in input().split(" ")]
    grid[h][w] = "#"

  # 横方向
  for h, w in lights:
    if ans_map_row[h][w]: continue

    for temp_w in range(w, W):
      if grid[h][temp_w] == "#": break
      ans_map_row[h][temp_w] = True

    for temp_w in reversed(range(0, w)):
      if grid[h][temp_w] == "#": break
      ans_map_row[h][temp_w] = True

  # 縦方向
  for h, w in lights:
    if ans_map_column[h][w]: continue

    for temp_h in range(h, H):
      if grid[temp_h][w] == "#": break
      ans_map_column[temp_h][w] = True

    for temp_h in reversed(range(0, h)):
      if grid[temp_h][w] == "#": break
      ans_map_column[temp_h][w] = True


  ans = 0
  for h in range(H):
    for w in range(W):
      if ans_map_column[h][w] or ans_map_row[h][w]: ans+=1
  # print(*ans_map_column, sep="\n")
  # print(*ans_map_row, sep="\n")
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
