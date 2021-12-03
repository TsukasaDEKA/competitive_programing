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
        input = """4
2 1 2
2 1 1
2 2 1
2 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 1
1 1
1 2
2 1 1
3 1 1 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
1 1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = set([input() for _ in range(N)])

  print(len(A))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()