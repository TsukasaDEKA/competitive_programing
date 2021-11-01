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
        input = """aba"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """ccc"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """xyz"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = list(set(input()))
  if len(S) == 1:
    print(1)
  elif len(S) == 2:
    print(3)
  elif len(S) == 3:
    print(6)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()