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

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  X = list(input())
  dictionary = defaultdict(int)
  for i in range(len(X)):
    dictionary[X[i]] = i
  N = int(input())
  S = [list(input()) for _ in range(N)]
  LIST = []
  for i in range(N):
    s = S[i]
    s = [dictionary[x] for x in s]
    LIST.append((s, i))

  LIST.sort()
  for i in range(N):
    print("".join(S[LIST[i][1]]))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()