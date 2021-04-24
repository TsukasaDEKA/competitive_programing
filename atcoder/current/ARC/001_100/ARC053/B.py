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
        input = """rokovoko"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """tomtom"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """vwxyz"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """succeeded"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 与えられた文字を任意に並び替えていいので、順番に意味はない。
  # なので Counter を使う
  # 奇数個の文字と偶数個の文字で扱いが違うっぽい
  from collections import Counter
  S = Counter(list(input()))
  word_count = 0
  odd_count = 0
  for key, val in S.items():
    if val%2:
      val -= 1
      word_count += 1
    odd_count += val//2
  if word_count == 0:
    print(odd_count*2)
    return
  odd_count//=word_count
  print(odd_count*2+1)

resolve()

if __name__ == "__main__":
    unittest.main()
