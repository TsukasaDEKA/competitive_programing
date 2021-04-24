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
        input = """atcoder"""
        output = """atcoderb"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """abc"""
        output = """abcd"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """zyxwvutsrqponmlkjihgfedcba"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """abcdefghijklmnopqrstuvwzyx"""
        output = """abcdefghijklmnopqrstuvx"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """z"""
        output = """za"""
        self.assertIO(input, output)

def resolve():
  num2alpha = lambda c: chr(c+97)
  inf = 10**10+1
  # S に一度も出てこない文字で最も小さい文字を調べる。
  S = list(input())
  set_S = set()
  for s in S: set_S.add(s)
  for i in range(26):
    alphabet = num2alpha(i)
    if alphabet not in set_S:
      print(*S, alphabet, sep="")
      return
  # 全ての文字が存在する場合、末尾の文字を一つ取って手元に置く。手元の文字の中で次の末尾の文字よりも大きい文字があれば置き換える、
  # そうでなかったら次の文字も取るってことを繰り返していく。
  len_S = len(S)
  set_S = set()
  for i in reversed(range(1, len_S)):
    set_S.add(S[i])
    for s in sorted(set_S):
      if s > S[i-1]:
        print(*S[:i-1], s, sep="")
        return

  print(-1)
resolve()

if __name__ == "__main__":
    unittest.main()
