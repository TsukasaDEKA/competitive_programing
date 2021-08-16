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
        input = """3 2
1 7 2
7 8 1
8 12 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
1 3 2
3 4 4
1 4 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 4
56 60 4
33 37 2
89 90 3
32 43 1
67 68 3
49 51 3
31 32 3
70 71 1
11 12 3"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush
  from collections import defaultdict
  # 簡単に足し引きすることでいけそう。
  N, C = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  events = []
  for s, t, c in A:
    heappush(events, (s, c))
    heappush(events, (t+0.5, -c))

  counter = defaultdict(int)
  count = 0
  ans = 0
  while events:
    s, c = heappop(events)
    if c >= 0:
      counter[c] += 1
      if counter[c] == 1: count+=1
    else:
      counter[-c] -= 1
      if counter[-c] == 0: count-=1
    ans = max(ans, count)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
