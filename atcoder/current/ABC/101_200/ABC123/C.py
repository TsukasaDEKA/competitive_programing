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
        input = """5
3
2
4
3
5"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
123
123
123
123
123"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10000000007
2
3
5
7
11"""
        output = """5000000008"""
        self.assertIO(input, output)

def resolve():
  # 最小値がボトルネックになるので、最小値だけ考えれば良い。
  N = int(input())
  A = min([int(input()) for _ in range(5)])

  print((N+A-1)//A+4)

resolve()

if __name__ == "__main__":
    unittest.main()
