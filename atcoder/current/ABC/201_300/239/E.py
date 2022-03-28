import sys
from io import StringIO
from tabnanny import check
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
1 2 3 4 5
1 4
2 1
2 5
3 2
1 2
2 1"""
        output = """4
5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 2
10 10 10 9 8 8
1 4
2 1
2 5
3 2
6 4
1 4
2 2"""
        output = """9
10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4
1 10 100 1000
1 2
2 3
3 4
1 4
2 3
3 2
4 1"""
        output = """1
10
100
1000"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  X = [int(x) for x in input().split(" ")]
  EDGES = [[] for _ in range(N)]
  for _ in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].append(B)
    EDGES[B].append(A)

  # 上位 20 個取っておけば大丈夫。

  nexts = deque()
  nexts.append(~0)
  nexts.append(0)
  ranking = [[] for _ in range(N)]
  checked = [False]*N
  checked[0] = True
  while nexts:
    # print(nexts)
    current = nexts.pop()
    # print(current+1 if current >= 0 else ~current+1)
    if current < 0:
      current = ~current
      temp = [X[current]]
      for i in EDGES[current]:
        for n in ranking[i]:
          temp.append(n)
      ranking[current] = sorted(temp, reverse=True)[:20]
      # print(ranking)
      continue

    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      nexts.append(~n)
      nexts.append(n)

  # print(ranking)
  for _ in range(Q):
    V, K = [int(x)-1 for x in input().split(" ")]
    print(ranking[V][K])


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()