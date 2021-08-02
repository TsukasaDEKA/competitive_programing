# import sys
# from io import StringIO
# import unittest

# class TestClass(unittest.TestCase):
#     maxDiff = None
#     def assertIO(self, input, output):
#         stdout, stdin = sys.stdout, sys.stdin
#         sys.stdout, sys.stdin = StringIO(), StringIO(input)
#         resolve()
#         sys.stdout.seek(0)
#         out = sys.stdout.read()[:-1]
#         sys.stdout, sys.stdin = stdout, stdin
#         self.assertEqual(out, output)

# import sys
# sys.setrecursionlimit(500*500)

# from math import gcd
# from functools import reduce
# from itertools import product
# from itertools import combinations
# from itertools import accumulate # 累積和作るやつ
# import numpy as np
# from collections import deque
# from collections import defaultdict
# from heapq import heappop, heappush

# alpha2num = lambda c: ord(c) - ord('a')
# num2alpha = lambda c: chr(c+97)
# popcnt = lambda x: bin(x).count("1")

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

import sys
env = "dev" if sys.argv[-1] == './Main.py' else "prd"

def resolve():
  # 適当な点から他の全ての点までの距離を図る。
  # 一番遠い点からまた他の全ての点までの距離を図る。
  # その結果、一番遠い点までの距離が答え。
  N = int(input())

  max_d = 0
  current_i = 1
  temp_i = current_i
  for i in range(1, N+1):
    if current_i == i: continue
    print("? {0} {1}".format(current_i, i))
    d = int(input())
    if max_d < d:
      temp_i = i
      max_d = d

  current_i = temp_i
  for i in range(1, N+1):
    if current_i == i: continue
    print("? {0} {1}".format(current_i, i))
    d = int(input())
    if max_d < d: max_d = d
  print("! {0}".format(max_d))
  sys.stdout.flush()

resolve()

# if __name__ == "__main__":
#   unittest.main()