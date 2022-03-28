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
        input = """1 2 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """13 1 4 3000"""
        output = """87058"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  R, G, B, N = map(int, input().split(" "))
  count = 0
  for r in range(N+1):
    for g in range(N+1):
      if N-(r*R+g*G) >= 0 and (N-(r*R+g*G))%B == 0:
        count += 1

  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()