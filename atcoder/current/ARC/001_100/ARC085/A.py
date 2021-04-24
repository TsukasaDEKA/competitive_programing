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
        input = """1 1"""
        output = """3800"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 2"""
        output = """18400"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 5"""
        output = """608000"""
        self.assertIO(input, output)

def resolve():
  # 何回実行するかを計算して、それに一回あたりの実行時間をかける。
  # ランダムで M 問正解する確率は 1/(2**M)。
  # 回数の期待値は 1/1/(2**M) = 2**M
  # M <= 100 なので pow (繰り返し二乗法) でやった方が安心
  N, M = map(int, input().split(" "))
  one_term = M*1900 + (N-M)*100
  print(pow(2**M)*one_term)

resolve()

if __name__ == "__main__":
    unittest.main()
