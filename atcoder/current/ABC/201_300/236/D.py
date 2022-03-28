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
        input = """2
4 0 1
5 3
2"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
5"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
900606388 317329110 665451442 1045743214 260775845 726039763 57365372 741277060 944347467
369646735 642395945 599952146 86221147 523579390 591944369 911198494 695097136
138172503 571268336 111747377 595746631 934427285 840101927 757856472
655483844 580613112 445614713 607825444 252585196 725229185
827291247 105489451 58628521 1032791417 152042357
919691140 703307785 100772330 370415195
666350287 691977663 987658020
1039679956 218233643
70938785"""
        output = """1073289207"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  N = int(input())
  A = []
  for i in range(2*N-1):
    A.append([0]*(i+1) + [int(x) for x in input().split(" ")])
  A.append([[0]*(2*N)])

  nexts = deque()
  for i in range(1, 2*N):
    bit = ((1<<2*N)-1)-(1<<i)-1
    nexts.append((A[0][i], bit))

  ans = 0
  while nexts:
    v, bit = nexts.popleft()
    if bit == 0:
      if ans < v: ans = v
      continue
    
    tar = [i for i in range(1, 2*N-1) if bit&(1<<i)]
    for i in tar:
      if bit&(1<<i):
        for j in range(i+1, 2*N):
          if bit&(1<<j):
            b = bit-(1<<j)-(1<<i)
            nexts.append((v^A[i][j], b))
      break
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()