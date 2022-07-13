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
        input = """6
AARCCC"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
AAAAA"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9
ARCARCARC"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush
  from collections import deque

  # 偶数回目の操作で切断が発生する。
  # A の連続 + R + C の連続を一つのブロックと考える。
  inf = 10**18+1
  N = int(input())
  S = [""] + list(input()) + [""]

  len_1_count = 0
  targets = []
  # 前から見て行ってブロックに分離する。
  current = ""
  for i in range(1, N):
    if S[i] == "R":
      index = i
      count_A = 0
      while S[index-1] == "A":
        count_A += 1
        index -= 1

      index = i
      count_C = 0
      while S[index+1] == "C":
        count_C += 1
        index += 1

      # print(count_A, count_C)
      size = min(count_A, count_C)
      if size == 1:
        len_1_count += 1

      if size > 1:
        targets.append(size)

  targets = deque(sorted(targets))

  # print(len_1_count)
  ans = 0
  for i in range(N):
    if len(targets) == 0:
      print(ans+len_1_count)
      return

    ans += 1
    if i%2 == 0:
      # 奇数回の操作では targets から取り出して操作する。
      t = targets.popleft()
      t -= 1
      if t == 1:
        len_1_count += 1
      else:
        targets.appendleft(t)
    else:
      # 偶数回の操作ではできるだけ len_1_count を使う。
      if len_1_count:
        len_1_count -= 1
      else:
        targets.popleft()
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()