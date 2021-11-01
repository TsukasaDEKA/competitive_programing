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
        input = """5
1 2
1 3
1 9
2 9
3 9
3 9 2 4 5 6 7 8"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 2
1 3
1 9
2 9
3 9
1 2 3 4 5 6 7 8"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """12
8 5
9 6
4 5
4 1
2 5
8 9
2 1
3 6
8 7
6 5
7 4
2 3
1 2 3 4 5 6 8 7"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """12
6 5
5 4
4 1
4 7
8 5
2 1
2 5
6 9
3 6
9 8
8 7
3 2
2 3 4 6 1 9 7 8"""
        output = """16"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  N = 9
  M = int(input())
  EDGES = [set() for _ in range(N+1)]
  for _ in range(M):
    u, v = [int(x) for x in input().split(" ")]
    EDGES[u].add(v)
    EDGES[v].add(u)

  P = [int(x) for x in input().split(" ")]
  # コマの種類が大事なのでコマ基準に変更する。
  blank = set(list(range(1, 10)))
  for p in P: blank.remove(p)
  # 開始時の状態の配列表現
  P.append(blank.pop())
  temp = 0
  for i in range(N):
    temp+= P[i] * pow(10, N-i-1)

  if temp == 123456789:
    print(0)
    return

  nexts = deque()
  nexts.append((temp, 0))
  cheched = set()
  while nexts:
    current, count = nexts.popleft()
    # 空のマスがどこと隣接しているか調べて、そこにあるマスと入れ替える。
    target = [int(x) for x in list(str(current))]
    blank = target[-1]
    for i in range(N-1):
      if target[i] in EDGES[blank]:
        temp = current
        index = temp - target[i]*pow(10, N-i-1) - blank + blank*pow(10, N-i-1) + target[i]

        if index in cheched: continue
        if index == 123456789:
          print(count+1)
          return
        cheched.add(index)
        nexts.append((index, count+1))
  print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()