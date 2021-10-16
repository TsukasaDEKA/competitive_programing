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
        input = """1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"""
        output = """abcdefghijklmnopqrstuvwxyz"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"""
        output = """bacdefghijklmnopqrstuvwxyz"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 11 12 16 25 17 18 1 7 10 4 23 20 3 2 24 26 19 14 9 6 22 8 13 15 21"""
        output = """eklpyqragjdwtcbxzsnifvhmou"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  num2alpha = lambda c: chr(c+96)

  P = [num2alpha(int(x)) for x in input().split(" ")]

  print("".join(P))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()