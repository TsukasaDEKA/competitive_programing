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
        input = """10 30 20 40"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 20 30 40"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  A, B, X, Y = map(int, input().split(" "))

  print("Yes" if X <= B and A <= Y else "No")

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
