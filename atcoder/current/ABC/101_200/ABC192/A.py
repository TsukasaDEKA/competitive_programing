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
        input = """140"""
        output = """60"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000"""
        output = """100"""
        self.assertIO(input, output)

def resolve():
  X = int(input())
  print(100-X%100)

resolve()

if __name__ == "__main__":
    unittest.main()
