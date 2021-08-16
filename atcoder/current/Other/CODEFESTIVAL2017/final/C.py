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
        input = """3
7 12 8"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
11 11"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
0"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
5"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # D の範囲は 12 個しかない。
  # 0 が一個でもあったら 0
  # 3 人以上同じ数字があった場合、必ず 0 になる。
  # 鳩の巣原理を考えると N >= 25 の時は必ず 0
  # N <= 24 なら全部のパターンで全探索で行けそう。
  from collections import Counter

  N = int(input())
  D = [int(x) for x in input().split(" ")]

  static_members = set()
  dynamic_memmbers = []
  D_sum = Counter(D)
  for k, v in D_sum.items():
    if v >= 3 or k == 0:
      print(0)
      return

    if v == 2:
      static_members.add(k)
      static_members.add(24-k)

    if v == 1:
      dynamic_memmbers.append(k)

  ans = 0
  for bit in range(1<<len(dynamic_memmbers)):
    tar = []
    for b in range(len(dynamic_memmbers)):
      if (bit>>b)&1: tar.append(dynamic_memmbers[b])
      else: tar.append(24-dynamic_memmbers[b])

    for s in static_members:
      tar.append(s)

    tar.sort()
    tar = [0]+tar+[24]
    temp = 25

    for i in range(len(tar)-1):
      temp = min(temp, abs(tar[i] - tar[i+1]))

    ans = max(ans, temp)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()