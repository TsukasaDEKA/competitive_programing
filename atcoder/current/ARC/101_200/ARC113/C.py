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
        input = """accept"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """atcoder"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """anerroroccurred"""
        output = """16"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """aacbbbc"""
        output = """6"""
        self.assertIO(input, output)


    def test_Sample_Input_5(self):
        input = """aacbbbcc"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # 右から順に数えていく。
  # インデックスを減らしていくのは少し手間なので逆順に並べ替え
  S = list(reversed(list(input())))
  ans = 0
  # 現在見ている文字より左側の文字をカウントする。
  count = defaultdict(int)
  count[S[0]] += 1
  for i in range(1, len(S)):
    if S[i-1] == S[i]:
      # 変更する文字を数える。(現在のインデックスから左側の文字の数 - 現在のインデックスから左側に含まれる現在見ている文字と同じ文字の数)
      ans += i - count[S[i]]
      # 現在の index より左側は全て同じ文字になるため、 count をクリアして現在見てる文字分カウントする。
      count.clear()
      count[S[i]] += i+1
    else:
      count[S[i]] += 1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
