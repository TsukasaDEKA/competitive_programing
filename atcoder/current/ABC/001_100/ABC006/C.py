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
        input = """3 9"""
        output = """1 1 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 23"""
        output = """1 3 3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 41"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1500 41"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)

def resolve():
  # 大人、老人、赤ちゃんの人数をそれぞれ A, B, C とすると、
  # A+B+C = N
  # 2*A + 3*B + 4*C = M
  # N <= 1500 で、間に仕切りを入れるので、1501C2 = 1501*1500 = 2,251,500
  # 全探索でいけそう。
  # 制約誤読してた・・・
  # N <= 10**5 なので全然間に合わない。
  # 2*N <= M <= 4*N なら必ず解ける。
  # M - 2*N で、余りを B + 2*C = M - 2*N で計算する。
  N, M = map(int, input().split(" "))

  if M < 2*N or 4*N < M:
    print("-1 -1 -1")
    return

  c = (M - 2*N) // 2
  b = (M - 2*N) % 2
  a = N - b - c
  print(a, b, c, sep=" ")
resolve()

if __name__ == "__main__":
    unittest.main()
