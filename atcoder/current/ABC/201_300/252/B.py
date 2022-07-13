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
        input = """5 3
6 8 10 7 10
2 3 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 2
100 100 100 1 1
5 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 1
100 1
2"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = set([int(x)-1 for x in input().split(" ")])

  max_ = max(A)
  for i in range(N):
    if A[i] == max_ and i in B:
      print("Yes")
      return

  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()