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
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1
1 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 7
1 2
2 3
3 4
4 2
5 6
6 7
7 5"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  # 複数の閉路にまたがっている点がある場合、0, 
  # グループ毎に 1 個の閉路が 1 個あれば 0K。複数個ある場合はだめ。
  # 2**最終的にグループの個数 になる。
  mod = 998244353
  N, M = map(int, input().split(" "))
  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    U, V = [int(x)-1 for x in input().split(" ")]
    EDGES[U].append(V)
    EDGES[V].append(U)

  checked = [False]*N
  nexts = deque()
  parents = [-1]*N
  group = 0
  for i in range(N):
    if checked[i]: continue
    checked[i] = True
    group += 1
    loop_count = 0
    nexts.append(i)
    while nexts:
      current = nexts.pop()
      for n in EDGES[current]:
        if checked[n]:
          if parents[current] != n:
            # print(i, current, n, loop_count)
            loop_count+=1
            if loop_count > 2:
              print(0)
              return
          continue
        checked[n] = True
        parents[n] = current
        nexts.append(n)
    if loop_count != 2:
      print(0)
      return
  print(pow(2, group, mod))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()