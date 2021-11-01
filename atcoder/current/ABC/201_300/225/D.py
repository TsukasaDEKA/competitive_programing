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
        input = """7 14
1 6 3
1 4 1
1 5 2
1 2 7
1 3 5
3 2
3 4
3 6
2 3 5
2 4 1
1 1 5
3 2
3 4
3 6"""
        output = """5 6 3 5 2 7
2 4 1
5 6 3 5 2 7
4 1 5 2 7
1 4
2 6 3"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  FRONT = [-1 for _ in range(N)]
  TAIL = [-1 for _ in range(N)]
  for i in range(Q):
    query = [int(x)-1 for x in input().split(" ")]
    if query[0] == 0:
      _, x, y = query
      FRONT[y] = x
      TAIL[x] = y

    if query[0] == 1:
      _, x, y = query
      FRONT[y] = -1
      TAIL[x] = -1

    if query[0] == 2:
      _, x = query
      while FRONT[x] >= 0:
        x = FRONT[x]

      ans = []
      while True:
        ans.append(x+1)
        x = TAIL[x]
        if x == -1:
          break
      print(len(ans), *ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()