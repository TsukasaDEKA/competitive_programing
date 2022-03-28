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
        input = """4
3 5 5"""
        output = """1 3 5 4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
4 8 8 2 5"""
        output = """4 4 8 2 2 5"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5
1 2 3 4"""
        output = """1 1 2 3 4"""
        self.assertIO(input, output)

def resolve():
  N, *K = int(input()), [int(x) for x in input().split(" ")]
  print(K[0], *(min(K[i-1:i+1]) for i in range(1, N-1)), K[-1])

# resolve()

if __name__ == "__main__":
    unittest.main()
