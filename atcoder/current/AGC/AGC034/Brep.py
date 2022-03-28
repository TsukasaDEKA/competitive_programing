import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """ABCABC"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """C"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """ABCACCBABCBCAABCB"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  # 連続する BC を T に置き換える。
  # 残った B, C を全て * に置き換える。
  # 後ろから見ていって、連続する T の数を数えていき、A がきたら答えに T の数を足していく。
  # * がきたら T の数をリセットする。
  S = input().replace('BC', 'T').replace('B', '*').replace('C', '*')

  ans = 0
  count = 0
  for s in S[::-1]:
    if s == "A": ans += count
    if s == "*": count = 0
    if s == "T": count += 1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()