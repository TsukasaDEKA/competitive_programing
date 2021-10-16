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
        input = """7
1 2 1 3 1 4 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
100"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 尺取り法を使う。
  # l = 0, r = 0 から初めて r を増やしていって、
  # l ~ r の間に特定の数字が 2 個以上含まれたら一旦 r を止めてその数字が 1 個になるまで l を動かして
  # 再度 r を動かして・・・と繰り返していく。
  # 区間に含まれる数字の管理は dict が楽。
  from collections import defaultdict

  N = int(input())
  A = [int(x) for x in input().split(" ")]
  l = r = 0 
  agg = defaultdict(int)
  count = 0
  ans = 0
  while r < N:
    agg[A[r]]+=1
    if agg[A[r]] == 1: count+=1

    while agg[A[r]] >= 2:
      agg[A[l]]-=1
      if agg[A[l]] == 0: count-=1
      l+=1

    if ans < count: ans = count
    r+=1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()