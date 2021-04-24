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
  # S を辞書配列化する。
  # T の i 文字目が S の何文字目にあるかを探してそれを記録する。
  # T の i+1 文字目が、上記の S 上の文字より後に存在するか、するなら何文字目なのかを確認する。
  # 存在しないなら S をもう一個付け足す処理をする (実際には付け足さない。)
  # O(S + T) くらいでできる多分。
  S = list(input())
  # 文字の存在確認用
  set_S = set(S)
  T = list(input())

  # S の 辞書配列を作成 (構築に時間がかかりすぎるかも)
  dicts_S = [defaultdict(int) for _ in range(len(S))]
  for i in reversed(range(len(S)-1)):
    # i 文字目から見た時に、最も近いアルファベット x のインデックスを記録する。
    for key, val in dicts_S[i+1].items():
      dicts_S[i][key] = val
    dicts_S[i][S[i+1]] = i+1
  
  # print(dicts_S)
  ans = 0

  S_i = 0
  if T[0] != S[0]:
    if T[0] not in set_S:
      print(-1)
      return
    S_i = dicts_S[0][T[0]]
  ans += S_i+1

  # print(T[0], ans)
  for i in range(1, len(T)):
    if T[i] not in set_S:
      print(-1)
      return
    # T の i 番目の文字が、現在見ている S の S_i 文字目以降で見つからない場合、S を追加するような処理をいれる。
    if T[i] not in dicts_S[S_i]:
      ans+=len(S)-1-S_i
      S_i = 0
      if T[i] in dicts_S[S_i] and T[i] != S[0]:
        S_i = dicts_S[S_i][T[i]]
      ans += S_i+1
    else:
      ans += dicts_S[S_i][T[i]] - S_i
      S_i = dicts_S[S_i][T[i]]
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
