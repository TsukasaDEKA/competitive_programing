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
        input = """3
abb"""
        output = """3
3
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """11
mississippi"""
        output = """11
16
14
12
13
11
9
7
4
3
4"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  S = list(input())
  

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()