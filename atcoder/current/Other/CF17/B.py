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
        input = """abac"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """aba"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """babacccabab"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """aaabbbccc"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """aaaabbbbcc"""
        output = """YES"""
        self.assertIO(input, output)


def resolve():
  # 自由に並び替えられる => 初めの並びは関係ないので、Counter を使う。
  from collections import Counter
  from collections import defaultdict

  S = {"a": 0, "b": 0, "c": 0}
  for key, value in Counter(input()).items():
    S[key] = value
  # a, b, c にそれぞれ対称性があるので、多い順から A, B, C とする。
  A, B, C = sorted(S.values(), reverse=True)
  # 2文字以上の回文なので、同じ文字が連続しちゃいけない。
  # aba みたいなのもダメ
  # abcabcabc・・・みたいにできないといけない。(abcab とか、途中で止めるのは有り)

  print("YES")  if A - C <= 1 else print("NO")
resolve()

if __name__ == "__main__":
    unittest.main()
