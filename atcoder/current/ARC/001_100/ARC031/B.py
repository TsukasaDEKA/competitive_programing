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

    def test_入力例1(self):
        input = """xxxxxxxxxx
xoooooooxx
xxoooooxxx
xxxoooxxxx
xxxxoxxxxx
xxxxxxxxxx
xxxxoxxxxx
xxxoooxxxx
xxoooooxxx
xxxxxxxxxx"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """xxxxxxxxxx
xoooooooxx
xxoooooxxx
xxxoooxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxoooxxxx
xxoooooxxx
xxxxxxxxxx"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
ooooxooooo
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx"""
        output = """YES"""
        self.assertIO(input, output)

def resolve():
  # 最初に陸地の個数を数える。
  # 海を一つ埋め立てて、そこから幅優先探索を行って、
  # 島の大きさが陸地の個数+1 になったら YES、
  # 全ての埋め立てパターンを試してみても島の大きさが陸地の個数+1 にならなかったら NO
  # 幅優先探索のコストが最悪 100 で、それを海の個数だけ行う。
  # 10000 未満の計算量でいけるので間に合いそう。
  from collections import deque
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  A = [list(input()) for _ in range(10)]

  land_count = 0
  for h in range(10):
    for w in range(10):
      if A[h][w] == "x": continue
      land_count += 1

  # 幅優先探索
  found_island = False
  for h in range(10):
    for w in range(10):
      if A[h][w] == "o": continue
      temp_count = 0
      checked = [[False]*10 for _ in range(10)]
      nexts = deque()
      nexts.append((h, w))
      while nexts:
        current_h, current_w = nexts.popleft()
        for i in range(4):
          h_ = current_h+dh[i]
          w_ = current_w+dw[i]
          if h_ >= 0 and h_ < 10 and w_ >= 0 and w_ < 10:
            if checked[h_][w_] or A[h_][w_] == "x": continue
            checked[h_][w_] = True
            temp_count += 1
            nexts.append((h_, w_))
      if temp_count == land_count:
        print("YES")
        return

  print("NO")

resolve()

if __name__ == "__main__":
    unittest.main()
