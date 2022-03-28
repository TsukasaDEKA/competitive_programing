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
1 2
2 3
3 1"""
        output = """2 2 0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1000000000 1000000000
1000000000 1000000000"""
        output = """0 1000000000"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  # 座標圧縮 imos
  N = int(input())
  A_B = [[int(x) for x in input().split(" ")] for _ in range(N)]
  day = set()
  for a, b in A_B:
    day.add(a)
    day.add(a+b)

  day = sorted(list(day))
  table = defaultdict(int)
  for i in range(len(day)):
    table[day[i]] = i

  imos = [0]*len(day)
  for a, b in A_B:
    imos[table[a]] += 1
    imos[table[a+b]] -= 1
  
  for i in range(1, len(imos)):
    imos[i] += imos[i-1]


  agg = defaultdict(int)
  for i in range(len(imos)-1):
    agg[imos[i]] += day[i+1]-day[i]
  
  ans = [0]*N
  for k in range(1, N+1):
    ans[k-1] = agg[k]
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()