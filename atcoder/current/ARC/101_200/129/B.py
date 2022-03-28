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
        input = """3
1 3
2 4
5 6"""
        output = """0
0
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
64 96
30 78
52 61
18 28
9 34
42 86
11 49
1 79
13 59
70 95"""
        output = """0
0
2
18
18
18
18
18
18
21"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush
  # グラフの合成問題。座標を圧縮する.
  # 最も離れている L, R との距離を求める。
  # R, L を別々に集計して
  inf = 10**18+1
  N = int(input())
  R = []
  L = []
  for _ in range(N):
    l, r = [int(x) for x in input().split(" ")]
    heappush(R, r)
    heappush(L, -l)
    r_, l_ = R[0], -L[0]
    # print(r_, l_, max((l_-r_+1)//2, 0))
    print(max((l_-r_+1)//2, 0))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()