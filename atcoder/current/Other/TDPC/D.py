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
        input = """2 6"""
        output = """0.416666667"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2"""
        output = """0.875000000"""
        self.assertIO(input, output)

def resolve():
  # サイコロを N 回振った時、出た目の積が D の倍数となる確率を求めよ
  # D <= 10**18 まである。多い。
  # 10**18 <= 2**60 (2**10 で大体 10**3 なので) になるので、最悪 60 回 2 と 3 と 5 で割り算すれば良い。
  # 余ったら確率は 0 になる。
  # サイコロの目には 1, 2, 3, 2*2, 5, 2*3 が含まれる。
  # D に 2, 3, 5 がいくつ含まれているか知りたい。
  N = int(input())
  N, D = map(int, input().split(" "))

  print(N)

# resolve()


if __name__ == "__main__":
    unittest.main()
