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
        input = """B"""
        output = """A"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """a"""
        output = """a"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """AA"""
        output = """No"""
        self.assertIO(input, output)


import re

def resolve():
  A = input()
  print("A" if re.match(r'[A-Z]', A) else "a")


if __name__ == "__main__":
    unittest.main()
