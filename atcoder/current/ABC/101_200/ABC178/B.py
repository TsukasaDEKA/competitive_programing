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
        input = """1 2 1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5 -4 -2"""
        output = """-6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """-1000000000 0 -1000000000 0"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

def resolve():
  A, B, C, D = map(int, input().split(" "))

  print(max(A*C, A*D, B*C, B*D))

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
