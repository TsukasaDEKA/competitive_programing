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
        input = """2"""
        output = """1 2 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3485"""
        output = """872 1012974 1539173474040"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4664"""
        output = """3498 3498 3498"""
        self.assertIO(input, output)

def resolve():
  # h, b, w <= 3500 なので、 三乗オーダーだと間に合わない。二乗オーダーだとギリギリ間に合いそう。(Python だと怪しいかも。)
  # 4/N=1/h + 1/n + 1/w を 式変形して、1/w = 4/N - 1/h - 1/n = (4 * n * h - N * n - N * h)/(N * h * n) なので w = (N * h * n)/(4 * n * h - N * n - N * h)
  # h, n を 1 ~ 3500 の間で回して、(h * n)/(4 * N * h * n) が整数になる組み合わせを探す。
  # h <= n を固定すれば 6125000 回の計算なので間に合う (かも)
  N = int(input())

  for h in range(1, 3500+1):
    for n in range(h, 3500+1):
      molecule = N * h * n
      denomi = 4 * n * h - N * n - N * h
      # print(molecule, denomi)
      if denomi <= 0: continue
      if molecule%denomi==0:
        print(n, h, molecule//denomi)
        return

resolve()

if __name__ == "__main__":
    unittest.main()
