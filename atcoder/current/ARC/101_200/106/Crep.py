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
        input = """5 1"""
        output = """1 10
8 12
13 20
11 14
2 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 -10"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M = map(int, input().split(" "))

  if N == 1 and M == 0:
    print(1, 2)
    return

  if N-M-2 < 0 or M < 0:
    print(-1)
    return

  ans = [[i*2, i*2+1] for i in range(1, N+1)]
  ans[M+1][0] = 1

  for a in ans:
    print(*a)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()