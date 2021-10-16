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
        input = """3
1 2
2 3"""
        output = """3
2
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 2"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
1 6
1 5
1 3
1 4
1 2"""
        output = """5
9
9
9
9
9"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  N = int(input())
  EDGES = [[] for _ in range(N+1)]
  for _ in range(N-1):
    A, B = [int(x) for x in input().split(" ")]
    EDGES[A].append(B)
    EDGES[B].append(A)

  ans = [0]*(N+1)
  # 子の個数を数える。
  children = [0]*(N+1)
  depth = [0]*(N+1)
  parent = [0]*(N+1)
  nexts = deque()
  nexts.append(-1)
  nexts.append(1)
  checked = [False]*(N+1)
  checked[0] = checked[1] = True
  while nexts:
    current = nexts.pop()
    if current < 0:
      current = -current
      for e in EDGES[current]:
        if e == parent[current]: continue
        children[current] += children[e]+1
      continue
    
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      parent[n] = current
      depth[n] = depth[current]+1
      nexts.append(-n)
      nexts.append(n)
  
  ans = [0]*(N+1)
  ans[1] = sum(depth)

  nexts.append(1)
  checked = [False]*(N+1)
  checked[0] = checked[1] = True
  while nexts:
    current = nexts.pop()
    if current != 1:
      i = current
      ans[i] = ans[parent[i]] - children[i] + (N-children[i]-2)

    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      nexts.append(n)

  for i in range(1, N+1):
    print(ans[i])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()