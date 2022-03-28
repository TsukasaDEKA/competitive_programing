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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)

def resolve():
  N, Q = map(int, input().split(" "))
  S = list(input())
  LEFT = [0]*N
  for i in range(1, N):
    LEFT[i] = LEFT[i-1]
    if S[i-1:i+1] == ["A", "C"]:LEFT[i]+=1
  # LEFT = [0]+LEFT
  RIGHT = [0]*N
  for i in range(N-2, -1, -1):
    RIGHT[i] = RIGHT[i+1]
    if S[i:i+2] == ["A", "C"]:RIGHT[i]+=1
  # RIGHT = RIGHT+[0]

  # print(LEFT, RIGHT)
  total = RIGHT[0]
  for i in range(Q):
    l, r = [int(x)-1 for x in input().split(" ")]
    # print(l, r, LEFT[l], RIGHT[r])
    print(total-LEFT[l]-RIGHT[r])
  # print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()