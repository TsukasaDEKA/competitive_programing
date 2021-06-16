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
        input = """4 3
3 5 6 7
2
5
3"""
        output = """2
9
4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 2
1 2 3 4 5
1
10"""
        output = """6
15"""
        self.assertIO(input, output)


def resolve():
  from bisect import bisect_left

  # 二分探索っぽい。
  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  count = [0]*N
  for i in range(N):
    count[i] = A[i]-(i+1)

  for _ in range(Q):
    K = int(input())
    i = bisect_left(count, K)
    if i == 0:
      print(K)
    else:
      print(A[i-1]+(K-count[i-1]))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
