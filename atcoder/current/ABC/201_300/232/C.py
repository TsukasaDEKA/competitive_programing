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
        input = """4 4
1 2
1 3
1 4
3 4
1 3
1 4
2 3
3 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 6
1 2
1 3
1 4
3 4
3 5
4 5
1 2
1 3
1 4
1 5
3 5
4 5"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 0"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  from itertools import permutations

  inf = 10**18+1
  N, M = map(int, input().split(" "))
  EDGES_T = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]
  EDGES_T.sort()
  EDGES_A = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]

  for P in permutations(range(N), N):
    new_edges = []
    for a, b in EDGES_A:
      new_edges.append(sorted([P[a], P[b]]))
    new_edges.sort()

    if new_edges == EDGES_T:
      print("Yes")
      return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()