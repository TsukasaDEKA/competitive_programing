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
        input = """2 2 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10 10"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 4 5"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  A, B, C = map(int, input().split(" "))


  print("Yes" if A**2 + B**2 < C**2 else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
