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
        input = """3 1 4
2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 3
1 2
1 3
2 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 3 100
1 2
4 5
2 3"""
        output = """428417047"""
        self.assertIO(input, output)


def resolve():
  mod = 998244353
  from collections import deque
  N, M, K = map(int, input().split(" "))

  INVALID_PATH = [set() for _ in range(N)]
  for M in range(M):
    U, V = [int(x)-1 for x in input().split(" ")]
    INVALID_PATH[U].add(V)
    INVALID_PATH[V].add(U)

  # K = 2

  field = [[0]*N for _ in range(K+1)]
  field[0][0] = 1
  nexts = set()
  nexts.add(0)
  for k in range(1, K+1):
    temp_nexts = set()
    for n in nexts:
      # print(n)
      # print(*field, sep="\n")

      for i in range(N):
        if i == n: continue
        if i in INVALID_PATH[n]: continue

        field[k][i]+=field[k-1][n]
        if field[k][i] > mod: field[k][i]%=mod
        if i not in temp_nexts:
          temp_nexts.add(i)
    
    nexts = temp_nexts
  # print(*field, sep="\n")
  print(field[-1][0])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()