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

  inf = 10**18+1
  N = int(input())
  A = [deque([int(x)-1 for x in input().split(" ")]) for _ in range(N)]
  count = 0
  fixed = 0
  while True:
    count+=1
    checked = [False]*N
    is_stack = True
    for i in range(N):
      if checked[i]: continue
      if A[i]:
        if i == A[A[i][0]][0]:
          checked[i] = checked[A[i][0]] = True
          fixed+=1
          is_stack = False
          _ = A[A[i][0]].popleft()
          _ = A[i].popleft()
        # print(i, A[A[i][0]][0], i == A[A[i][0]][0], A)

    if is_stack:
      if fixed < N*(N-1)//2: print(-1)
      else: print(count)
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()