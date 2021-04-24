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
        input = """4 5
##...
.##..
..##.
...##"""
        output = """Possible"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3
###
..#
###
#..
###"""
        output = """Impossible"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 5
##...
.###.
.###.
...##"""
        output = """Impossible"""
        self.assertIO(input, output)

def resolve():
  # 幅優先探索で右と下だけの移動でゴールに辿りついたのかを判定する。
  # ゴールにたどり着いたのは保証されてて、上や左に行く動作を行っていないので、
  # 幅優先探索をして、分岐を見つけたら Impossible、最後までいけたら Possible
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  H, W = map(int, input().split(" "))
  A = [[x=="#" for x in list(input())] for _ in range(H)]

  from collections import deque

  checked = [[False]*W for _ in range(H)]
  checked[0][0] = True
  nexts = deque()
  nexts.append((0, 0))
  while nexts:
    h, w = nexts.popleft()
    count = 0
    for i in range(4):
      h_= h + dh[i]
      w_= w + dw[i]
      if h_ >= 0 and h_ < H and w_ >= 0 and w_ < W:
        if not checked[h_][w_] and A[h_][w_]:
          if i <= 1:
            print("Impossible")
            return
          checked[h_][w_]=True
          count+=1
          nexts.append( (h_, w_) )

    if count != 1 and h != H-1 and w != W-1:
      print("Impossible")
      return
  print("Possible")
resolve()

if __name__ == "__main__":
    unittest.main()
