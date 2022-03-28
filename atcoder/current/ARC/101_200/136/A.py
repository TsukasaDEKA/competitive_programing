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
CBAA"""
        output = """CAAB"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
A"""
        output = """A"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
BBBCBB"""
        output = """ABCA"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
BBBBBB"""
        output = """AAA"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """6
BBBBBA"""
        output = """AAAB"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """6
AAABBA"""
        output = """AAAAA"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  N = int(input())
  S = list(input())
  stack = deque()
  stack.append({"A": 0, "B": 0})
  # BB はそのまま A にする
  # BA となってる場合は位置を入れ替えることができる。
  for i in range(N):
    if S[i] == "C":
      stack.append({"A": 0, "B": 0})
    else:
      val = stack.pop()
      val[S[i]]+=1
      stack.append(val)

  ans = []
  while stack:
    temp = ""
    val = stack.popleft()
    temp += "A"*(val["A"]+val["B"]//2)
    temp += "B"*(val["B"]%2)
    ans.append(temp)
  print(*ans, sep="C")
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()