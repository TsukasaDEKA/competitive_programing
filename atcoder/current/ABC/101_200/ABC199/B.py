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
        input = """2
3 2
7 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 5 3
10 7 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
3 2 5
6 9 8"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]

  l = 0
  r = inf
  for i in range(N):
    l = max(l, A[i])
    r = min(r, B[i])
  print(max(0, r - l + 1))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
