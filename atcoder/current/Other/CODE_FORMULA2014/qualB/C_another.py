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
        input = """abcdef
fedcba"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """abababab
babababa"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """nt
nt"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """pqqq
pqqq"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvxyzw
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """abcdef
ghijkl"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """abc
cab"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_7(self):
        input = """abcde
bcdea"""
        output = """NO"""
        self.assertIO(input, output)

def resolve():
  from itertools import combinations
  from collections import defaultdict
  # 一度文字毎に集計する。
  # 集計後、条件を満たすか判定する。
  S = list(input())
  T = list(input())

  agg_S = defaultdict(list)
  temp_S = []
  temp_T = []
  for i in range(len(S)):
    agg_S[S[i]].append(i)
    if S[i] != T[i]:
      temp_S.append(S[i])
      temp_T.append(T[i])
    # 位置が一致しないインデックスが 7 個以上であれば NO
    if len(temp_S) > 6:
      print("NO")
      return

  has_same_later = False
  for val in agg_S.values():
    if len(val) >= 2:
      has_same_later = True


  if S == T and has_same_later:
    print("YES")
    return

  # 全探索を行う。
  indexes = list(range(len(temp_S)))

  for tar1 in combinations(indexes, 2):
    # print(temp_S, temp_T)
    temp_S[tar1[0]], temp_S[tar1[1]] = temp_S[tar1[1]], temp_S[tar1[0]]
    if temp_S == temp_T:
      print("YES")
      return

    for tar2 in combinations(indexes, 2):
      temp_S[tar2[0]], temp_S[tar2[1]] = temp_S[tar2[1]], temp_S[tar2[0]]
      if temp_S == temp_T and has_same_later:
        print("YES")
        return

      for tar3 in combinations(indexes, 2):
        temp_S[tar3[0]], temp_S[tar3[1]] = temp_S[tar3[1]], temp_S[tar3[0]]
        if temp_S == temp_T:
          print("YES")
          return
        temp_S[tar3[0]], temp_S[tar3[1]] = temp_S[tar3[1]], temp_S[tar3[0]]
      temp_S[tar2[0]], temp_S[tar2[1]] = temp_S[tar2[1]], temp_S[tar2[0]]
    temp_S[tar1[0]], temp_S[tar1[1]] = temp_S[tar1[1]], temp_S[tar1[0]]
  print("NO")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()