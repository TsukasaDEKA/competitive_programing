from os import sep
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
        input = """4 5 2
xoooo
oooox
ooooo
oxxoo"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 5 2
ooooo
oxoox
oooox
oxxoo"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 6 3
oooooo
oooooo
oooooo
oooooo
oxoooo
oooooo
oooooo
oooooo"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  # 45°回転して累積和？
  # 違うっぽい
  R, C, K = map(int, input().split(" "))
  S = [list(input()) for _ in range(R)]
  countL = [[0]*(C+1) for _ in range(R)] + [[0]*(C+1)]
  for i in range(R):
    count = 0
    for j in range(C):
      if S[i][j] == "o": count+=1
      else: count = 0
      countL[i][j] = count

  countR = [[0]*(C+1) for _ in range(R)] + [[0]*(C+1)]
  for i in range(R):
    count = 0
    for j in reversed(range(C)):
      if S[i][j] == "o": count+=1
      else: count = 0
      countR[i][j] = count

  countD = [[0]*(C+1) for _ in range(R)] + [[0]*(C+1)]
  for j in range(C):
    count = 0
    for i in range(R):
      if S[i][j] == "o": count+=1
      else: count = 0
      countD[i][j] = count


  countU = [[0]*(C+1) for _ in range(R)] + [[0]*(C+1)]
  for j in range(C):
    count = 0
    for i in reversed(range(R)):
      if S[i][j] == "o": count+=1
      else: count = 0
      countU[i][j] = count

  ans = 0
  for i in range(K-1, R-K+1):
    for j in range(K-1, C-K+1):
      for k in range(K):
        # print(countL[i-k][j], countR[i-k][j], countL[i+k][j], countR[i+k][j])
        if min(countL[i-k][j], countR[i-k][j], countL[i+k][j], countR[i+k][j]) < K-k: break
        if min(countU[i][j-k], countD[i][j-k], countU[i][j+k], countD[i][j+k]) < K-k: break
      else:
        ans+=1
  print(ans)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()