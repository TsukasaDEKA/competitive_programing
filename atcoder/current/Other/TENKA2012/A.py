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
        input = """0"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """45"""
        output = """1836311903"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  # 大人兎と兎の総数を別々に持っておく。
  # N <= 45 なので愚直にやっても間に合いそう。
  adult = [0]*(N+1)

  if N <= 1:
    print(1)
    return
  adult[2] = 1
  total = 1
  for n in range(N+1):
    total += adult[n]
    if n+1 < N+1: adult[n+1]+=adult[n]
    if n+2 < N+1: adult[n+2]+=adult[n]

  print(total)

resolve()

if __name__ == "__main__":
    unittest.main()
