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
        input = """3 2
1 2 3"""
        output = """1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """11 5
3 7 2 5 11 6 1 9 8 10 4"""
        output = """2
3
3
5
6
7
7"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush

  inf = 10**18+1
  N, K = map(int, input().split(" "))
  P = [int(x) for x in input().split(" ")]
  heap = []
  for i in range(K):
    heappush(heap, P[i])

  ans = [heap[0]]
  for i in range(K, N):
    # print(heap)
    if P[i] < heap[0]:
      ans.append(heap[0])
    else:
      _ = heappop(heap)
      heappush(heap, P[i])
      ans.append(heap[0])

  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()