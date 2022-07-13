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
        input = """436204751575440756541724746755
347475575404531645424640344414
556644445442451553264555436757
761235545455474254546631467555
356447405421445153457656535564
014274425356522445253477726464
311765446655556346633757446600
471744514426443445162555525455
616053450444473274742055767455
254124557527462423444450075637
046546764557475436717475255501
752005462554554414031525515356
452524742177476245065554577605
664465643742341605007655253777
444571276444165545442447340356
435050335454565235025507452540
467560030465475447567644441426
735730577745561712541450443547
472675153755474445700540444544
507472724556677621365747544757
535177720776402476665547676174
636275455643650141456764547131
164624553536572554544165746536
521574724335644274433544442556
576732703453654464555315065544
656244747015464523316444145414
555646775254464367454454067475
665624154657072514445150474444
570004746554540445465051654541
635504417414262014475547424275"""
        output = """30"""
        self.assertIO(input, output)

# import sys
# sys.setrecursionlimit(500*500)

# from math import gcd
# from functools import reduce
# # product('ABCD', repeat=2) => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# from itertools import product
# # permutations('ABCD', 2) => AB AC AD BA BC BD CA CB CD DA DB DC
# from itertools import permutations
# # combinations('ABCD', 2) => AB AC AD BC BD CD
# from itertools import combinations
# from itertools import accumulate # 累積和作るやつ
# import numpy as np
# from collections import deque
# from collections import defaultdict
# from heapq import heappop, heappush
# from bisect import bisect_left
# # 0埋めされた二進数表現
# f'{9:05b}'

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]


def resolve():
  # パネルの種類は 3 種類。それを回転させたものになる。
  # 0 ~ 3 のパネルの取りうる値は 4 種類
  # 4 ~ 7 のパネルの取りうる値は 2 種類
  # マスの数は 30 * 30 の 900 個
  # パネルを回転させた際に線路の切断が発生する可能性がある。
  # 2 sec 制限があるので注意する。
  # 直線タイルが鍵になりそう ()
  # 一旦外周から渦巻き状に見ていく。
  # 直線タイルだけを見ていって、その外側とどうやっても接続できない状態なのであれば外壁に沿った状態に変更する。

  rotate = [1, 2, 3, 0, 5, 4, 7, 6]
  inf = 10**18+1
  H, W = 30, 30
  ans = [["0"]*W for _ in range(H)]
  rails_origin = [list(map(int, list(input())))+[-1] for h in range(H)] + [[-1]*(H+1)]
  # print(*rails_origin, sep="\n", file=sys.stderr)
  rails_ans = [[rails_origin[h][w] for w in range(W+1)] for h in range(H+1)]

  # 一旦外壁だけ整える。
  for w in range(1, W-1):
    if rails_ans[0][w] >= 6:
      rails_ans[0][w] = 6
    if rails_ans[H-1][w] >= 6:
      rails_ans[H-1][w] = 6

  for h in range(1, H-1):
    if rails_ans[h][0] >= 6:
      rails_ans[h][0] = 7
    if rails_ans[h][W-1] >= 6:
      rails_ans[h][W-1] = 7

  if rails_ans[0][0] <= 3: rails_ans[0][0] = 2
  if rails_ans[0][0] == 5: rails_ans[0][0] = 4
  if rails_ans[0][W-1] <= 3: rails_ans[0][W-1] = 1
  if rails_ans[0][W-1] == 4: rails_ans[0][W-1] = 5
  if rails_ans[H-1][0] <= 3: rails_ans[H-1][0] = 3
  if rails_ans[H-1][0] == 4: rails_ans[H-1][0] = 5
  if rails_ans[H-1][W-1] <= 3: rails_ans[H-1][W-1] = 0
  if rails_ans[H-1][W-1] == 5: rails_ans[H-1][W-1] = 4

  # 直線レールを見た時にその外側が水平、垂直であればそれに合わせた方が良さそう。
  for h in range(1, H-1):
    for w in range(1, W-1):
      if rails_ans[h][w] >= 6 and rails_ans[h-1][w] == 7:
        rails_ans[h][w] = 7
        continue
      if rails_ans[h][w] >= 6 and rails_ans[h][w-1] == 6:
        rails_ans[h][w] = 6

  for h in range(H-2, 0, -1):
    for w in range(W-2, 0, -1):
      if rails_ans[h][w] >= 6 and rails_ans[h+1][w] == 7:
        rails_ans[h][w] = 7
        continue
      if rails_ans[h][w] >= 6 and rails_ans[h][w+1] == 6:
        rails_ans[h][w] = 6

  # 閉路を切るのは得点が下がるリスクがあるため、既に連結済みのレールについて考えてみる。
  # 確率的に 2x3 とか 2*4 とかの閉路を作ることができる配置はいくつか存在しそう。
  # なのでパターンマッチングを試してみる。
  # 四角形を作る処理を汎用化できそう。
  for length_h in range(2, 15):
    for length_w in range(2, 15):
      for h in range(H-length_h+1):
        for w in range(W-length_w+1):
          top, bottom = h, h+length_h-1
          left, right = w, w+length_w-1
          # 作成できるか確認
          # 端がカーブを含むか?
          can_create = True
          for h_ in [top, bottom]:
            for w_ in [left, right]:
              if rails_ans[h_][w_] >= 6:
                can_create = False

          # 端以外が全て直線か？
          for h_ in [top, bottom]:
            for w_ in range(left+1, right):
              if rails_ans[h_][w_] <= 5:
                can_create = False

          for h_ in range(top+1, bottom):
            for w_ in [left, right]:
              if rails_ans[h_][w_] <= 5:
                can_create = False

          if not can_create:
            continue
          
          # 作成処理
          # 端を全部内側に向ける。
          if rails_ans[top][left] <= 3: rails_ans[top][left] = 2
          if rails_ans[top][left] == 5: rails_ans[top][left] = 4
          if rails_ans[top][right] <= 3: rails_ans[top][right] = 1
          if rails_ans[top][right] == 4: rails_ans[top][right] = 5
          if rails_ans[bottom][left] <= 3: rails_ans[bottom][left] = 3
          if rails_ans[bottom][left] == 4: rails_ans[bottom][left] = 5
          if rails_ans[bottom][right] <= 3: rails_ans[bottom][right] = 0
          if rails_ans[bottom][right] == 5: rails_ans[bottom][right] = 4

          # 端以外を全て縦にする。

          for h_ in [top, bottom]:
            for w_ in range(left+1, right):
              rails_ans[h_][w_] = 7

          if length_w == 2: continue
          for h_ in range(top+1, bottom):
            for w_ in [left, right]:
              rails_ans[h_][w_] = 6


  # 回転回数を記録する。
  for h in range(H):
    for w in range(W):
      # 回転させる回数を数える。
      count = 0
      current = rails_origin[h][w]
      while current != rails_ans[h][w]:
        current = rotate[current]
        count+=1
      ans[h][w] = count

  ans_str = ""
  for a in ans:
    ans_str += "".join([str(x) for x in a])
  print(ans_str)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()