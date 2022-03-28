import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """2 1 1 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 2 100 1"""
        output = """101"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 100 1 100"""
        output = """199"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 1 1 100"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
  A, B, X, Y = map(int, input().split(" "))
  diff = abs(A-B) 
  if A <= B:
    print(X+(diff)*min(2*X, Y))
  else:
    print(X+(diff-1)*min(2*X, Y))
resolve()


if __name__ == "__main__":
    unittest.main()
