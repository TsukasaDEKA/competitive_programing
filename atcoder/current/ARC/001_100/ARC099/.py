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
        input = """4 3
2 3 1 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 3
7 3 1 8 4 6 2 5"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  print((N-1+(K-2))//(K-1))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()