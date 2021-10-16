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
1 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 1 2 3 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
4 23 75 0 23 96 50 100"""
        output = """221"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  inf = 101
  # 遅延評価セグ木だと思いきや、要素数が小さいので愚直でいけそう。
  N = int(input())
  H = [int(x) for x in input().split(" ")]
  # 最小値を探す => i 番目が h になったらその要素を削除して残りの要素を分離して stack に積んでいく、というのを繰り返す。
  stack = deque()
  stack.append(H)
  ans = 0
  while stack:
    current = stack.pop()
    add_val = min(current)
    ans += add_val

    temp = []
    for h in current:
      if h == add_val:
        if temp:
          stack.append(temp)
          temp = []
      else:
        temp.append(h-add_val)
    else:
      if temp: stack.append(temp)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()