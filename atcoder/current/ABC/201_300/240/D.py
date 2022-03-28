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
        input = """5
3 2 3 2 2"""
        output = """1
2
3
4
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
2 3 2 3 3 3 2 3 3 2"""
        output = """1
2
3
4
5
3
2
3
1
0"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  que = deque()
  count = 0
  for a in A:
    count += 1
    if que:
      if que[-1][0] == a:
        que[-1].append(a)
        if len(que[-1]) == a:
          count -= len(que[-1])
          _ = que.pop()
      else:
        que.append([a])
    else:
      que.append([a])
    print(count)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()