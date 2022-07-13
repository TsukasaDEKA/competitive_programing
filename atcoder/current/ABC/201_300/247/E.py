import imp
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
        input = """4 3 1
1 2 3 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 2 1
1 3 2 4 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 1 1
1 1 1 1 1"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 8 1
2 7 1 8 2 8 1 8 2 8"""
        output = """36"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # まず、X より大きく、 Y より小さい値で数列を分割する。
  # 次にその数列上で L を固定して二分探索すればよさそう。
  inf = 10**18+1
  N, X, Y = map(int, input().split(" "))
  A = [0]+[int(x) for x in input().split(" ")]+[X+1]

  break_line = []
  for i in range(N+2):
    if A[i] > X or A[i] < Y:
      break_line.append(i)
 
  ans = 0
  B = len(break_line)
  for i in range(B-1):
    L = break_line[i]+1
    R = break_line[i+1]
    # ここから尺取り法

    agg = defaultdict(int)
    r = L
    for l in range(L, R):
      while r < R and not (agg[X] > 0 and agg[Y] > 0):
        agg[A[r]] += 1
        r += 1

      if agg[X] > 0 and agg[Y] > 0:
        ans += R-r+1

      agg[A[l]] -= 1
  print(ans)
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()