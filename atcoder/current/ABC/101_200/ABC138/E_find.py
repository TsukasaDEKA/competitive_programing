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
        input = """contest
son"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """contest
programming"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """contest
sentence"""
        output = """33"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """cc
cccc"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # find で書いてみる。
  S = input()
  # 文字の存在確認用
  set_S = set(list(S))
  T = list(input())

  ans = 0
  # 最初の文字だけ S の頭から検索したいので、-1 スタート
  S_i = -1
  for i in range(len(T)):
    if T[i] not in set_S:
      print(-1)
      return

    temp_S_i = S_i
    S_i = S.find(T[i], min(S_i+1, len(S)))
    if S_i != -1:
      ans += S_i - temp_S_i
    else:
      ans += len(S[temp_S_i+1:])
      S_i = S.find(T[i])
      ans += S_i+1

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
