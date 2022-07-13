import sys
from io import StringIO
import unittest

from numpy import true_divide

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
tanaka taro
tanaka jiro
suzuki hanako"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
aaa bbb
xxx aaa
bbb yyy"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
tanaka taro
tanaka taro"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3
takahashi chokudai
aoki kensho
snu ke"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  S = [input().split(" ") for _ in range(N)]

  for i in range(N):
    s, t = S[i]
    s_f, t_f = False, False
    for j in range(N):
      if i == j: continue
      s_, t_ = S[j]
      if s == s_ or s == t_: s_f = True
      if t == s_ or t == t_: t_f = True
      if s_f and t_f:
        print("No")
        return

  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()