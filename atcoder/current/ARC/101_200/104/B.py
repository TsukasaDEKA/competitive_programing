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
        input = """4 AGCT"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 ATAT"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 AAATACCGCG"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  N, S = input().split(" ")
  N = int(N)
  S = list(S)
  agg = {"A": [0]*(N+1), "T": [0]*(N+1), "C": [0]*(N+1), "G": [0]*(N+1)}
  for i in range(1, N+1):
    for key in agg.keys():
      agg[key][i] = agg[key][i-1]
      if S[i-1] == key: agg[key][i]+=1

  ans = 0
  for i in range(N):
    for j in range(i+1, N+1):
      if agg["A"][i] - agg["A"][j] != agg["T"][i] - agg["T"][j]: continue
      if agg["G"][i] - agg["G"][j] != agg["C"][i] - agg["C"][j]: continue
      ans += 1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()