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
        input = """2
3
4
0"""
        output = """5
2
1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  used = set()
  candidates = list(range(1, 2*N+2))
  for _ in range(N+1):
    while candidates[-1] in used:
      candidates.pop()
    ans = candidates.pop()
    used.add(ans)
    print(ans)
    used.add(int(input()))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()