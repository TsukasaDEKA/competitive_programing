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
        input = """4 50
80 60 40 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 90
89 89 89"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 22
6 37"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, P = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  count = 0
  for i in range(N):
    if A[i] < P:
      count+=1
  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()