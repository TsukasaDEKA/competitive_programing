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
        input = """4
1 2 3
2 2
1 3 4
2 3"""
        output = """4
8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 1000000000 1000000000
2 1000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  inf = 10**18+1
  Q = int(input())

  que = deque()
  for i in range(Q):
    query = [int(x) for x in input().split(" ")]
    if query[0] == 1:
      x, c = query[1:]
      que.append([x, c])
    else:
      c = query[-1]
      ans = 0
      while c > 0:
        x, c_ = que[0]
        count = min(c, c_)
        ans += x*count
        c -= count
        if c_ <= count:
          que.popleft()
        else:
          que[0][1] -= count

      print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()