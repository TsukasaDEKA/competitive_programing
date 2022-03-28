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
2 3
1 3
1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
2 3 4
1 3 4
4 1 2
3 1 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
2 3
3 1
1 2"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  # キューに入れて貪欲？
  from collections import deque
  import copy

  inf = 10**18+1
  N = int(input())
  A = [deque([sorted([int(x)-1, i]) for x in input().split(" ")]) for i in range(N)]
  count = 0
  target = set()
  for i in range(N):
    target.add(i)

  POOL = set()
  while target:
    count+=1
    temp = set()
    for t in target:
      i, j = A[t].popleft()
      if (i, j) in POOL:
        POOL.remove((i, j))
        if len(A[i]): temp.add(i)
        if len(A[j]): temp.add(j)
      else:
        POOL.add((i, j))
    target = temp

  for i in range(N):
    if len(A[i]):
      print(-1)
      return
  else:
    print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()