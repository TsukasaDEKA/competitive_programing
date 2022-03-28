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
        input = """3 3
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(M)]
  for i in range(10**(N-1) if N!=1 else 0, 10**N):
    j = [int(x) for x in list(str(i))]
    for s, c in A:
      if j[s-1] != c: break
    else:
      print(i)
      return

  print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()