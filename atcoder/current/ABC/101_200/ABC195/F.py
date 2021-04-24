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
        input = """2 4"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """123456789000 123456789050"""
        output = """2125824"""
        self.assertIO(input, output)

def resolve():
  # A, B の範囲が広すぎる。
  # B-A が 72 なのでいけるかも
  A, B = map(int, input().split(" "))

  print()

# resolve()

if __name__ == "__main__":
    unittest.main()
