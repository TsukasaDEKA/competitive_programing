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
        input = """6
3 1 2 4 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
3 3 3 3 4 4 4 5 5 5"""
        output = """20"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N = int(input())
  A = [int(x) for x in input().split(" ")]
  candidate = set()
  agg = defaultdict(int)
  for i in range(N):
    agg[A[i]]+=1
    if agg[A[i]] >= 2:
      candidate.add(A[i])
  candidate = sorted(list(candidate), reverse=True)

  if len(candidate) == 0:
    print(0)
    return
  if len(candidate) == 1:
    if agg[candidate[0]] < 4:
      print(0)
      return
    print(candidate[0]**2)
    return
  if agg[candidate[0]] < 4:
    print(candidate[0]*candidate[1])
    return
  print(candidate[0]**2)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()