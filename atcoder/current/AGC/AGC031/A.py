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
        input = """4
abcd"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
baa"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
abcab"""
        output = """17"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter, defaultdict

  mod = 10**9 + 7
  # 出現する文字の個数を数える。特定の文字種に対して、その文字を取らない、その同一文字種の文字の内からどれかを取るという選択肢がある。
  # 空の文字列はカウントできないので、最後に -1 をする点に注意する。
  # 例えば aaabb の場合、 a: 3, b: 2 なので、(3+1)*(2+1) - 1 = 11 になる。
  N = int(input())
  S = input()

  collection = Counter(S)
  ans = 1
  for val in collection.values():
    ans*=val+1
  print((ans-1)%mod)

resolve()

if __name__ == "__main__":
    unittest.main()
