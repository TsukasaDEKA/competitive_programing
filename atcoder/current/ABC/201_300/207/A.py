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

    def test_入力例_1(self):
        input = """3 4 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 6 6"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """99 99 98"""
        output = """198"""
        self.assertIO(input, output)


def resolve():
  A, B, C = map(int, input().split(" "))

  print(max(A+B, B+C, C+A))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
