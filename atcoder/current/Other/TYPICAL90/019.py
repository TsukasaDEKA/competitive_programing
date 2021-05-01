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
        input = """3
6 2 3 9 8 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 3 5 5 3 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 2 4 8 16 32 64 128"""
        output = """85"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """15
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32"""
        output = """207"""
        self.assertIO(input, output)

def resolve():
  # Ai とペアにできる組み合わせは A(i+k) (k は奇数)
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
