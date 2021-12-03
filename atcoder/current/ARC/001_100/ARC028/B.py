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
        input = """5 2
4 5 3 1 2"""
        output = """2
1
3
5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3
4 5 3 1 2"""
        output = """2
1
3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 1
2 3 1"""
        output = """1
1
3"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush

  N, K = map(int, input().split(" "))
  X = [int(x) for x in input().split(" ")]
  ans = []
  for i in range(K):
    heappush(ans, (-X[i], i+1))
  
  print(ans[0][1])
  for i in range(K, N):
    x, j = heappop(ans)
    x *= -1
    if X[i] < x:
      x, j = X[i], i+1

    heappush(ans, (-x, j))
    print(ans[0][1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()