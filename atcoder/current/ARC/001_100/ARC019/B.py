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
        input = """ARC"""
        output = """73"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """S"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """NOLEMONNOMELON"""
        output = """350"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """AARCA"""
        output = """123"""
        self.assertIO(input, output)

def resolve():
  # 元の文字列が回文じゃなくて、
  # 一文字変更すると回文になってしまうパターンと
  # どんなに変更しても回文にならないパターンで少し変わってくる。
  # ABCDEはどの一文字をどのように変更しても回文にはならない。
  # ABCDAは B や D を変更すると回文になる場合がある。
  # 半分で折り返して、前半分と後ろ半分の違いが丁度 0, 1, 2以上に分けて考えるか。
  # 奇数の場合、真ん中の文字は、
  # 前半分と後ろ半分の違いが 0 => いくら変更しても回文になる。
  # 前半分と後ろ半分の違いが 1 以上 => いくら変更しても回文にならない。
  # 同じ文字に変更するのはありなのか？
  # ABCA = 25 + 24 + 24 + 25

  S = list(input())
  front = S[:len(S)//2]
  end = S[:(len(S)-1)//2:-1]
  diff = 0
  # print(len(S)//2, len(front), len(end))
  for i in range(len(S)//2):
    if front[i] != end[i]: diff += 1
  
  if diff == 0:
    ans = len(S)*25
    if len(S)%2: ans -= 25
  elif diff == 1:
    ans = len(S)*25 - 2
  else:
    ans = len(S)*25
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
