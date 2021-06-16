import sys
from io import StringIO
from types import new_class
import unittest


class TestClass(unittest.TestCase):
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
1 2
2 3
3 2"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4
1 2
2 3
3 4
4 1"""
        output = """16"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  from collections import deque

  N, M = map(int, input().split(" "))
  EDGES = [set() for _ in range(N)]
  for _ in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].add(B)

  ans = N
  nexts = deque()
  for start in range(N):
    nexts.append(start)
    checked = [False]*N
    checked[start] = True
    while nexts:
      current = nexts.popleft()
      for n in EDGES[current]:
        if checked[n]: continue
        checked[n] = True
        ans += 1
        nexts.append(n)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
