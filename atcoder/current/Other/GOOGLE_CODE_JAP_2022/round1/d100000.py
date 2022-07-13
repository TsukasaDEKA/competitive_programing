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
4
6 10 12 8
6
5 4 5 4 4 4
10
10 10 7 6 7 4 4 5 7 4
1
10"""
        output = """Case #1: 4
Case #2: 5
Case #3: 9
Case #4: 1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())

  for t in range(1, T+1):
    N = int(input())
    A = sorted([int(x) for x in input().split(" ")])
    current = 0
    for i in range(N):
      if A[i] >= current+1:
        current += 1
    print("Case #{0}: {1}".format(t, current))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()