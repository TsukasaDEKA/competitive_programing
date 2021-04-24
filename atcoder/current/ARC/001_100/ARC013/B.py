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
        input = """2
10 20 30
20 20 20"""
        output = """12000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
10 20 30
20 20 20
30 20 10"""
        output = """12000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
10 20 30
20 20 20
30 20 10
10 40 10"""
        output = """16000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
10 10 10
11 1 1"""
        output = """1100"""
        self.assertIO(input, output)


def resolve():
  # ソートして、それぞれの列の最大値をとっる
  C = int(input())
  items = [sorted([int(x) for x in input().split(" ")]) for _ in range(C)]

  N = M = L = 0
  for n, m, l in items:
    N = max(N, n)
    M = max(M, m)
    L = max(L, l)

  print(N*M*L)

resolve()

if __name__ == "__main__":
    unittest.main()


