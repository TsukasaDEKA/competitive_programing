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
        input = """6
5
CODE JAM MIC EEL ZZZZZ
6
CODE JAM MIC EEL ZZZZZ EEK
2
OY YO
2
HASH CODE
6
A AA BB A BA BB
2
CAT TAX"""
        output = """Case #1: ZZZZZJAMMICCODEEEL
Case #2: IMPOSSIBLE
Case #3: IMPOSSIBLE
Case #4: IMPOSSIBLE
Case #5: BBBBBAAAAA
Case #6: IMPOSSIBLE"""
        self.assertIO(input, output)

def resolve():
  alpha2num = lambda c: ord(c) - ord('A')
  num2alpha = lambda c: chr(c+65)
  from collections import defaultdict
  from itertools import permutations
  T = int(input())

  for t in range(1, T+1):
    # 先頭の文字と末尾の文字で集計を取ったときのことを考える。
    # 全部のパターンを試して成り立つか確認する。
    N = int(input())
    S = [x for x in input().split(" ")]
    # 外部に露出していない文字について考える。
    # 外部に露出していない文字が他の Si に含まれていた時点で IMPOSSIBLE になる。
    # まずはそれを確認する。
    agg_S = [defaultdict(list) for _ in range(N)]
    valid = True
    for i in range(N):
      S_ = S[i]
      agg = defaultdict(list)
      for i in range(len(S_)):
        if len(agg[S_[i]]) == 0:
          agg[S_[i]].append(i)
        else:
          if agg[S_[i]][-1] < i-1:
            valid = False
            break
          agg[S_[i]].append(i)
      else:
        agg_S[i] = agg
        continue
      break

    # 不可能な文字列だった場合、抜ける。
    if not valid:
      print("Case #{0}: {1}".format(t, "IMPOSSIBLE"))
      continue

    # 途中に変な結合が行われていないか確認する。
    for i in range(N):
      for a in range(26):
        s = num2alpha(a)
        if len(agg_S[i][s]) == 0: continue
        if agg_S[i][s][0] == 0: continue
        if agg_S[i][s][-1] == len(S[i])-1: continue

        for j in range(N):
          if i == j: continue
          if len(agg_S[j][s]) != 0:
            valid = False
            break

    # 不可能な文字列だった場合、抜ける。
    if not valid:
      print("Case #{0}: {1}".format(t, "IMPOSSIBLE"))
      continue

    # 文字 X が先頭と末尾のどちらかにある場合がそれぞれ 2 つあれば IMPOSSIBLE
    agg_char = [defaultdict(list) for _ in range(26)]
    for i in range(N):
      S_ = S[i]
      if S_[0] == S[-1]:
        agg_char[alpha2num(S_[0])][2].append(i)
        continue
      agg_char[alpha2num(S_[0])][0].append(i)
      if len(agg_char[alpha2num[S[0]]][0]) >= 2:
        valid = False
        break
      agg_char[alpha2num(S_[-1])][1].append(i)
      if len(agg_char[alpha2num(S_[-1])][1]) >= 2:
        valid = False
        break
    

    # それぞれの文字で末尾先頭を結合していく。
    # 実際に結合するのではなく、インデックスどうしを結合する。
    to_ = [-1]*N
    for i in range(N):
      if to_[i] >= 0: continue
      current = i
      S_ = S[i]
      if len(agg_char[alpha2num(S_[-1])][1]):
        


    for i in range(26):
        


# resolve()

if __name__ == "__main__":
  unittest.main()