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

    def test_Sample_Input_1(self):
        input = """4
2
1 5
4
1 4 2 3
5
10 10 10 10 10
4
7 1 3 1000000"""
        output = """Case #1: 2
Case #2: 3
Case #3: 5
Case #4: 2"""
        self.assertIO(input, output)

def resolve():
  # シミュレートしていこう。
  from collections import deque

  inf = 10**18+1
  T = int(input())


  for t in range(1, T+1):
    N = int(input())
    A = deque([int(x) for x in input().split(" ")])
    # 小さい方から貪欲にとっていく？
    # 一旦 貪欲にやっていって、大丈夫そう。
    ans = 0
    prev = -1
    current = 0
    for i in range(N):
      if A[0] == A[-1]:
        current = A.pop()
      elif A[0] > A[-1]:
        current = A.pop()
      else:
        current = A.popleft()

      if current >= prev:
        ans += 1
      prev = max(prev, current)
      # print("{0} : {1}, {2}".format(t, A, ans))
    print("Case #{0}: {1}".format(t, ans))

resolve()

if __name__ == "__main__":
  unittest.main()