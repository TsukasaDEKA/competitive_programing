import sys
from io import StringIO
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

    def test_入力例_1(self):
        input = """4
1 2
2 3
2 4"""
        output = """3 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
1 3
2 4
3 5
2 5
3 6"""
        output = """1 2 6"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  # 任意の点で DFS やって、深さの偶奇で分けていく。
  # 偶数か奇数のどっちか大きい方から N/2 個取れば良い。
  inf = 10**18+1
  N = int(input())

  PATH = [set() for _ in range(N)]
  for i in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    PATH[A].add(B)
    PATH[B].add(A)

  odd = set()
  even = set()

  nexts = deque([0])
  checked = [False]*N
  checked[0] = True
  step = [0]*N

  while nexts:
    current = nexts.pop()
    if step[current]%2: odd.add(current)
    else: even.add(current)

    for n in PATH[current]:
      if checked[n]: continue
      checked[n] = True

      step[n] = step[current]+1
      nexts.append(n)

  odd = list(odd)
  even = list(even)
  if len(odd) >= N//2:
    print(*[x+1 for x in odd[:N//2]], sep=" ")
  else:
    print(*[x+1 for x in even[:N//2]], sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
