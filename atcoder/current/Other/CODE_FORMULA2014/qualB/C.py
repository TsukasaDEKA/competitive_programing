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

#     def test_Sample_Input_1(self):
#         input = """abcdef
# fedcba"""
#         output = """YES"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """abababab
# babababa"""
#         output = """NO"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """nt
# nt"""
#         output = """NO"""
#         self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """pqqq
# pqqq"""
#         output = """YES"""
#         self.assertIO(input, output)

#     def test_Sample_Input_5(self):
#         input = """abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvxyzw
# abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"""
#         output = """YES"""
#         self.assertIO(input, output)

#     def test_Sample_Input_6(self):
#         input = """abcdef
# ghijkl"""
#         output = """NO"""
#         self.assertIO(input, output)

#     def test_Sample_Input_6(self):
#         input = """abc
# cab"""
#         output = """NO"""
#         self.assertIO(input, output)

    def test_Sample_Input_7(self):
        input = """abcde
bcdea"""
        output = """YES"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # 一度文字毎に集計する。
  # 集計後、条件を満たすか判定する。
  S = list(input())
  T = list(input())

  target_indexes = []
  agg_S = defaultdict(list)
  agg_T = defaultdict(list)
  unmached_S = []
  unmached_T = []
  for i in range(len(S)):
    agg_S[S[i]].append(i)
    agg_T[T[i]].append(i)
    if S[i] != T[i]:
      target_indexes.append(i)
      unmached_S.append(S[i])
      unmached_T.append(T[i])

    # 位置が一致しないインデックスが 7 個以上であれば NO
    if len(target_indexes) > 6:
      print("NO")
      return

  unmached_S.sort()
  unmached_T.sort()
  # 位置が違う文字を見た時に種類が一致しなかった時、NO
  if unmached_S != unmached_T:
    print("NO")
    return

  # 同じ文字で入れ替えが可能な場合は可能。
  if len(target_indexes) == 0 or len(target_indexes) == 3:
    for val in agg_S.values():
      if len(val) >= 2:
        print("YES")
        return
    print("NO")
    return

  # 2, 3 文字であればどんな状態であっても可能。
  if len(target_indexes) == 2:
    print("YES")
    return

  agg_tar_S = defaultdict(list)
  agg_tar_T = defaultdict(list)
  for i in target_indexes:
    agg_tar_S[S[i]].append(i)
    agg_tar_T[T[i]].append(i)

  # # なんかグラフっぽく解けそう。
  # # 4 の場合、ペアが 2 個かつ他に同じ文字が無い場合のみ NO。
  if len(target_indexes) == 4:
    if S[target_indexes[0]] == T[agg_tar_S[T[target_indexes[0]]][0]]:
      for val in agg_S.values():
        if len(val) >= 2:
          break
      else:
        print("NO")
        return
    print("YES")
    return

  if len(target_indexes) == 5:
    # 1 ペア作れれば YES
    for i in target_indexes:
      for j in agg_tar_S[T[i]]:
        if T[i] == S[j] and S[i] == T[j]:
          print("YES")
          return
    print("NO")
    return

  if len(target_indexes) == 6:
    # ペアを 3 個作れれば YES
    for i in target_indexes:
      for j in agg_tar_S[T[i]]:
        if T[i] == S[j]: break
      else:
        print("NO")
        return
    print("YES")
    return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()