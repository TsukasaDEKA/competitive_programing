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
        input = """4
0 1 1 0"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 0 0 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
0 0 0 1"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  # それぞれの操作を A, B と呼ぶ。
  # 前方には A で追加した要素、後方には B で追加した要素が集まっていることになる。
  # 最初の操作はどちらでも同じ結果になるので、A を行ったと仮定した時、
  # 操作は A を一回行って B を 0 回以上行うというのを合計操作回数が N 回になるまで繰り返すことだと言える。
  # A の間に行われた B を一つのブロックだとする (長さ 0 もあり得る) と、
  # A の個数と B のブロックの個数は同じになる。
  # それを左右から除外していき、矛盾なく最後まで除外できれば Yes、できなければ No になる。
  from collections import deque

  N = int(input())
  A = deque([int(x) for x in input().split(" ")])
  fliped = False
  while A:
    # 除外対象。フリップしてる場合は 1、していない場合は 0。
    taeget = 1 if fliped else 0
    if A[0] != taeget:
      print("No")
      return

    # B で追加した要素のブロックを除外する。
    while A[-1] == taeget:
      A.pop()
      if len(A) == 0:
        print("Yes")
        return
    # A で追加した要素を除外する。
    A.popleft()
    fliped = ~fliped

  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()