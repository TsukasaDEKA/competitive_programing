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

    def test_入力例1(self):
        input = """4 4
##..
##..
..##
..##"""
        output = """possible
#...
....
....
...#"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 4
###.
####
..##
..##"""
        output = """possible
##..
....
...#
...#"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 4
###.
##.#
..##
..##"""
        output = """impossible"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, -1, -1,  0,  0,  1,  1,  1]
  dw = [-1,  0,  1, -1,  1, -1,  0,  1]
  # 周辺のマスが全て "#" だったら Fixed フラグを立てる。
  # 全てのマスが Fixed にできれば possible、そうでなければ impossible
  H, W = map(int, input().split(" "))
  S = [list(input()) for _ in range(H)]

  fixed = [[False]*W for _ in range(H)]
  ans = [["."]*W for _ in range(H)]
  for h in range(H):
    for w in range(W):
      # if fixed[h][w]: continue
      if S[h][w] == ".":
        fixed[h][w] = True
        continue

      count = 0
      for i in range(8):
        h_ = h + dh[i]
        w_ = w + dw[i]
        if h_ >= 0 and h_ < H and w_ >= 0 and w_ < W:
          if S[h_][w_] == "#": count+=1
          else: break
        else: count+=1

      if count == 8:
        ans[h][w] = "#"
        fixed[h][w] = True
        for i in range(8):
          h_ = h + dh[i]
          w_ = w + dw[i]
          if h_ >= 0 and h_ < H and w_ >= 0 and w_ < W:
            fixed[h_][w_] = True
          
  # print(*fixed, sep="\n")
  for h in range(H):
    for w in range(W):
      if not fixed[h][w]:
        print("impossible")
        return

  print("possible")
  for a in ans:
    print(*a, sep="")

resolve()

if __name__ == "__main__":
    unittest.main()
