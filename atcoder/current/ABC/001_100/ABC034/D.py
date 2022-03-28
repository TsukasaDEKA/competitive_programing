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
  from collections import deque

  N, K = map(int, input().split(" "))
  W_P = sorted([[int(x) for x in input().split(" ")] for _ in range(N)], key=lambda x: x[1], reverse=True)

  w, p = W_P[0]
  tar = set(list(range(1, N)))
  for _ in range(K-1):
    temp_p = 0
    temp_i = 0
    for i in tar:
      w_, p_ = W_P[i]
      if (w_*p_+w*p)/(w_+w) > temp_p:
        temp_p = (w_*p_+w*p)/(w_+w)
        temp_i = i
    w_, p_ = W_P[temp_i]
    p = (w_*p_+w*p)/(w_+w)
    w+=w
    tar.remove(temp_i)
  print(p)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()