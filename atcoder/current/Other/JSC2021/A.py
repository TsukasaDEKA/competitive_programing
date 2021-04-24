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
        input = """100 200 100"""
        output = """199"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """103 971 593"""
        output = """5590"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000 1 1"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
  X, Y, Z = map(int, input().split(" "))

  print((Y*Z-1)//X)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
