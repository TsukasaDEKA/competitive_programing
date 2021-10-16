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
        input = """bacdefghijklmnopqrstuvwxzy
4
abx
bzz
bzy
caa"""
        output = """bzz
bzy
abx
caa"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """zyxwvutsrqponmlkjihgfedcba
5
a
ab
abc
ac
b"""
        output = """b
a
ac
ab
abc"""
        self.assertIO(input, output)

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)

def resolve():
  from collections import defaultdict
  inf = 10**18+1
  X = list(input())
  x_dict = defaultdict(str)
  rev_ = defaultdict(str)
  for i in range(26):
    x_dict[X[i]] = num2alpha(i)
    rev_[num2alpha(i)] = X[i]

  N = int(input())
  S = [list(input()) for _ in range(N)]
  S_new = []
  for s in S:
    temp = ""
    for e in s:
      temp += x_dict[e]
    S_new.append(temp)
  S_new.sort()

  # print(S_int)
  for s in S_new:
    temp = ""
    for e in s:
      temp+=rev_[e]
    print(temp)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()