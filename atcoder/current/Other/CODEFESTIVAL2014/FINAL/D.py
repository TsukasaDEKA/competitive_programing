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

    def test_入力例1(self):
        input = """10"""
        output = """6 3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3921225"""
        output = """101 5"""
        self.assertIO(input, output)

def resolve():
  # パスカルの三角形は淵から 2 番目の数が段数 - 1 になる。
  A = int(input())
  print(A+1, 2, sep=" ")

# resolve()

if __name__ == "__main__":
    unittest.main()
