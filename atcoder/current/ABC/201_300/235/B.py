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
1 5 10 4 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
100 1000 100000"""
        output = """100000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
27 1828 1828 9242"""
        output = """1828"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  for i in range(N-1):
    if A[i] < A[i+1]: continue
    print(A[i])
    return

  print(A[-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()