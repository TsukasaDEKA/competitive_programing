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
        input = """4
2 4
4 3
9 3
100 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
8 20
1 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
10 1
2 1
4 1
6 1
8 1"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # 変換してソートして愚直に取得
  inf = 10**18+1
  N = int(input())
  X = [[int(x) for x in input().split(" ")] for _ in range(N)]
  ranges = []
  for i in range(N):
    x, l = X[i]
    ranges.append([x-l, x+l])
  ranges.sort(key=lambda x: x[1])
  ans = 0
  r = -inf
  for i in range(N):
    if ranges[i][0] >= r:
      ans+=1
      r = ranges[i][1]
  print(ans)



import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()