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
        input = """9
RGBGGBGBR"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
RGBRGB"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 文字列を順に取り出して並び替えるとき、
  # 前にくっつけるか後ろにくっつけるか選ぶ。
  # 頑張れば奇数個の文字を全種類 1 個だけ残して他を消すってできるんじゃないか？
  # RGRBRGRBRGRB と来た時、
  # RG => G => GB => GBR => BR => R => => GRB みたいにできそう
  from collections import Counter
  N = int(input())
  S = Counter(list(input()))
  ans = 0
  for val in S.values(): ans += val%2

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
