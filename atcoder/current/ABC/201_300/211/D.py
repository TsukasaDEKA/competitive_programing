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
        input = """4 5
2 4
1 2
2 3
1 3
3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 3
1 3
2 3
2 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7 8
1 3
1 4
2 3
2 4
2 5
2 6
5 7
6 7"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
  inf =10**18
  mod = 10**9+7
  N, M = map(int, input().split(" "))
  PATH = [set() for _ in range(N)]
  for i in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    PATH[A].add(B)
    PATH[B].add(A)

  pattarn = [0]*N
  pattarn[0] = 1
  checked = [False]*N
  checked[0] = True
  step = [inf]*N
  step[0] = 0
  # 自分のパターン数を配っていく。
  from collections import deque
  nexts = deque()
  nexts.append(0)
  while nexts:
    current = nexts.popleft()

    for n in PATH[current]:
      if step[n] > step[current]: pattarn[n] += pattarn[current]
      if checked[n]: continue
      checked[n] = True
      step[n] = step[current]+1

      if pattarn[n]>=mod: pattarn[n]%=mod
      nexts.append(n)

  # print(pattarn)
  print(pattarn[-1]%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()