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
        input = """3 3
1 2 1
2 3 1
1 3 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
1 2 1
2 3 1
1 3 5"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 3
2 1 1
2 3 5
3 4 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 3
8 7 100
7 9 100
9 8 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """100 0"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  # DFS で探索しながら座標を振っていく。
  # 途中で座標に矛盾があったら NO
  # 多重辺は存在しない。
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    L, R, D = [int(x) for x in input().split(" ")]
    L -= 1
    R -= 1
    EDGES[L].append((R, D))
    EDGES[R].append((L, -D))
  
  nexts = deque()
  checked = [False]*N
  X = [inf]*N
  for i in range(N):
    if checked[i]: continue
    nexts.append(i)
    X[i] = 0
    while nexts:
      current = nexts.popleft()
      for other, d in EDGES[current]:
        if checked[other]:
          if X[other] != X[current]+d:
            print("No")
            return
          continue
        checked[other] = True
        X[other] = X[current]+d
        nexts.append(other)

  print("Yes")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()