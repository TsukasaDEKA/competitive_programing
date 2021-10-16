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
        input = """8
1 4
1 3
1 2
1 1
3
2
1 0
2"""
        output = """1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9
1 5
1 5
1 3
2
3
2
1 6
3
2"""
        output = """5
3
5"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  from heapq import heappop, heappush

  inf = 10**18+1
  Q = int(input())

  que = deque()
  heapq = []

  for _ in range(Q):
    query = [int(x) for x in input().split(" ")]
    if query[0] == 1:
      x = query[1]
      que.append(x)

    if query[0] == 2:
      if heapq:
        ans = heappop(heapq)
      else:
        ans = que.popleft()
      print(ans)

    if query[0] == 3:
      while que:
        heappush(heapq, que.popleft())

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()