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

#     def test_Sample_Input_1(self):
#         input = """2
# 3
# 1 2
# 2 3
# 3 3
# 5
# 1 2
# 1 3
# 2 3
# 3 3
# 999999999 1000000000"""
#         output = """Yes
# No"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
5
1 5
1 6
2 2
2 5
2 3"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  from heapq import heappop, heappush
  # 終端が短い方から愚直で行けそう。
  T = int(input())

  for _ in range(T):
    N = int(input())
    # if N == 5:
    #   print("Yes")
    #   continue

    L_R = deque(sorted([[int(x) for x in input().split(" ")] for _ in range(N)]))

    pq = []
    i = L_R[0][0]
    while i <= 10**9+1:
      if len(L_R) > 0:
        while L_R[0][0] == i:
          l, r = L_R.popleft()
          heappush(pq, r)
          if len(L_R)==0:
            break
      
      r = heappop(pq)
      if r < i:
        print("No")
        break

      i+=1
      if len(pq) == 0:
        if len(L_R) == 0:
          print("Yes")
          break
        i = L_R[0][0]

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()