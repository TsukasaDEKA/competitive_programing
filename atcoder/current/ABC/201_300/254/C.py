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
        input = """5 2
3 4 1 3 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3
3 4 1 3 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 5
1 2 3 4 5 5 10"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  agg_A = [[] for _ in range(K)]
  for i in range(K):
    agg_A[i] = sorted([a for a in A[i::K]])
  
  for i in range(1, N):
    if agg_A[i%K][i//K] < agg_A[(i-1)%K][(i-1)//K]:
      print("No")
      return
  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()