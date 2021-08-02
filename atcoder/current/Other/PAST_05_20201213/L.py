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
        input = """7
adbabcd
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
ababaa
aba"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
zzzzzz
abc"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
aababa
aba"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
  # 前から消した方がいい場合と後ろから消した方がいい場合がある。
  # スタックで解く
  # 真ん中から消していきたい。
  from collections import deque
  N = int(input())
  S = input()
  T = input()

  ans = 0
  stack = deque()
  for s in S:
    if s != T[0] and s != T[1] and s != T[2]:
      stack.clear()
      continue

    if s == T[0]:
      stack.append(s)
      continue
    
    if stack:
      current = stack.pop()
      # print(current)
      if current[-1] == T[1] and s == T[2]:
        ans+=1
        continue
      if current[-1] == T[0] and s == T[1]:
        current+=T[1]
      stack.append(current)
      # stack.clear()
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
