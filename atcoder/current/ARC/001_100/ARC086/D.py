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
-2 5 -1"""
        output = """2
2 3
3 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
-1 -3"""
        output = """1
2 1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 絶対値が一番大きい要素を全てに足す事で全てを 正 or 負 にすることができる。
  # 全てが揃っていたらあとは簡単。
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  min_a_i, max_a_i = 0, 0
  for i in range(N):
    if A[min_a_i] > A[i]: min_a_i = i
    if A[max_a_i] < A[i]: max_a_i = i

  ans = []
  if A[min_a_i] < 0 and A[max_a_i] > 0:
    tar_i = max_a_i
    if abs(A[min_a_i]) <= abs(A[max_a_i]):
      tar_i = max_a_i
    else:
      tar_i = min_a_i

    for i in range(N):
      if i == tar_i: continue
      ans.append((tar_i, i))
      A[i] += A[tar_i]

  if min(A) < 0:
    for i in range(N-2, -1, -1):
      ans.append((i+1, i))
      A[i] += A[i+1]
  elif max(A) > 0:
    for i in range(1, N):
      ans.append((i-1, i))
      A[i] += A[i-1]

  print(len(ans))
  for a in ans:
    x, y = a
    x += 1
    y += 1
    print(x, y, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()