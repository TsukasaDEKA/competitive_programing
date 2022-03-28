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
        input = """4 4 6"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 7 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 3 3"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  N, A, B = map(int, input().split(" "))
  min_ = A*(N-1)+B
  max_ = B*(N-1)+A
  print(max(max_-min_+1, 0))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()