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
        input = """1"""
        output = """213456"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5"""
        output = """234561"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """22"""
        output = """615234"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000000"""
        output = """345612"""
        self.assertIO(input, output)

def resolve():
  # N <= 10**9 なので単純にシミュレートしていったら間に合わない。
  # 30 回操作を行うことで一周するので、N%30 でシミュレート指定けば良い。
  N = int(input())
  cards = [0, 1, 2, 3, 4, 5, 6]
  N%=30
  for i in range(N):
    cards[i%5+1], cards[i%5+2] = cards[i%5+2], cards[i%5+1]
  print(*cards[1:], sep="")

resolve()

if __name__ == "__main__":
    unittest.main()
