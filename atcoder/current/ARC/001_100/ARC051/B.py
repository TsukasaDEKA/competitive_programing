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
        input = """1"""
        output = """1 1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3"""
        output = """4 5"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """12"""
        output = """314159265 358979323"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """40"""
        output = """314159265 358979323"""
        self.assertIO(input, output)


def resolve():
  K = int(input())

  if K == 0:
    print(1, 0)
    return

  ans = (2, 1)
  for _ in range(K-1):
    ans = (ans[0] + ans[1], ans[0])
  print(*ans)

resolve()

if __name__ == "__main__":
    unittest.main()
