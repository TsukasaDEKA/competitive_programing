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
abcde"""
        output = """e"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
a"""
        output = """a"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  S = list(input())

  print(S[-1])


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()