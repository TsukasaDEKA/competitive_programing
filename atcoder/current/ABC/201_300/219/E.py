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
        input = """1 0 0 0
0 0 1 0
0 0 0 0
1 0 0 0"""
        output = """1272"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  from collections import deque
  popcnt = lambda x: bin(x).count("1")
  # 全探索かな。
  # 条件を満たす組み合わせを効率よく探索したい。
  # 堀じゃなくマスに注目
  # 全探索して条件を満たす場合だけを数える。
  A = [[int(x) for x in input().split(" ")] for _ in range(4)]

  ans = 0
  nexts = deque()
  for bit in range(1, 1<<16):
    # 家が一致するかチェック
    for h in range(4):
      for w in range(4):
        # 家が選ばれていない場合 break
        if A[h][w] == 1 and bit&(1<<(4*h+w)) == 0: break
      else: continue
      break
    else:
      # 全てが連結か確認する。
      cnt = popcnt(bit)
      temp_map = [[0]*4 for _ in range(4)]

      for h in range(4):
        for w in range(4):
          if bit&(1<<(4*h+w)):
            temp_map[h][w] = 1
            if nexts: continue
            nexts.append((h, w))

      checked = [[False]*4 for _ in range(4)]
      h, w = nexts.popleft()
      checked[h][w] = True
      nexts.append((h, w))
      temp_count = 0
      while nexts:
        h, w = nexts.popleft()
        temp_count+=1
        for i in range(4):
          h_ = h+dh[i]
          w_ = w+dw[i]
          if h_ < 0 or h_ >= 4 or w_ < 0 or w_ >= 4: continue
          if temp_map[h_][w_] == 0: continue 
          if checked[h_][w_]: continue
          checked[h_][w_] = True
          nexts.append((h_, w_))

      if temp_count != cnt:
        continue


      checked = [[False]*4 for _ in range(4)]
      for h in range(4):
        for w in range(4):
          if h == 0 or w == 0 or h == 3 or w == 3:
            if temp_map[h][w] == 0:
              nexts.append((h, w))
              checked[h][w] = True

      temp_count = 0
      while nexts:
        h, w = nexts.popleft()
        temp_count+=1
        for i in range(4):
          h_ = h+dh[i]
          w_ = w+dw[i]
          if h_ < 0 or h_ >= 4 or w_ < 0 or w_ >= 4: continue
          if temp_map[h_][w_] == 1: continue 
          if checked[h_][w_]: continue
          checked[h_][w_] = True
          nexts.append((h_, w_))

      if temp_count != 16-cnt:
        continue

      # 自己交差がないか確認する。
      for h in range(3):
        for w in range(3):
          if temp_map[h][w] == 1:
            if temp_map[h+1][w+1] == 1 and temp_map[h][w+1] == 0 and temp_map[h+1][w] == 0:
              break
          if temp_map[h][w] == 0:
            if temp_map[h+1][w+1] == 0 and temp_map[h][w+1] == 1 and temp_map[h+1][w] == 1:
              break
        else: continue
        break
      else:
        ans+=1
      # ans+=1

  print(ans)

import sys
sys.setrecursionlimit(500*500)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()