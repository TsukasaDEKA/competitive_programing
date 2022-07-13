from collections import defaultdict
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
        input = """3 2
100 15
300 20
200 30"""
        output = """25.000000000"""
        self.assertIO(input, output)

def resolve():
  # DP っぽい。
  # 愚直でいける・・・？
  inf = 10**9+1
  from collections import deque

  N, K = map(int, input().split(" "))
  W_P = sorted([[int(x) for x in input().split(" ")] for _ in range(N)], key=lambda x: x[1], reverse=True)

  used = set([0])
  total, p = W_P[0]
  if p == 0:
    print(0)
    return
  solt = total*p/100
  W_P[0] = [inf, 0]
  K-=1
  for _ in range(K):
    tar = 0
    conce = 0
    for j in range(N):
      w, p = W_P[j]
      if w == inf: continue
      s = w*p/100
      if (s+solt)/(total+w) > conce:
        tar = j
        conce = (s+solt)/(w+total)
    w, p = W_P[tar]
    total+=w
    solt+=w*p/100
    W_P[tar] = [inf, 0]
  print(solt/total*100)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()