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
        input = """2 3
GCP
PPP
CCC
PPC"""
        output = """3
1
2
4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
GC
PG
CG
PP"""
        output = """1
2
3
4"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  A = [list(input()) for _ in range(2*N)]
  # (勝った数, インデックス)
  rank = [(0, x) for x in range(2*N)]
  for m in range(M):
    temp = []
    for k in range(N):
      a_count, a_i = rank[2*k]
      b_count, b_i = rank[2*k+1]

      if A[a_i][m] == "G" and A[b_i][m] == "C": a_count-=1
      if A[a_i][m] == "C" and A[b_i][m] == "P": a_count-=1
      if A[a_i][m] == "P" and A[b_i][m] == "G": a_count-=1
      if A[b_i][m] == "G" and A[a_i][m] == "C": b_count-=1
      if A[b_i][m] == "C" and A[a_i][m] == "P": b_count-=1
      if A[b_i][m] == "P" and A[a_i][m] == "G": b_count-=1
      temp.append((a_count, a_i))
      temp.append((b_count, b_i))

    rank = temp
    rank.sort()
    # print(m, rank)
  ans = []
  for i in range(2*N):
    _, i = rank[i]
    ans.append(i+1)
    
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()