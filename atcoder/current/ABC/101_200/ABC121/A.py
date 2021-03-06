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
        input = """3 2
2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 4
2 4"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  h, w = map(int, input().split(" "))

  print((H-h)*(W-w))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()