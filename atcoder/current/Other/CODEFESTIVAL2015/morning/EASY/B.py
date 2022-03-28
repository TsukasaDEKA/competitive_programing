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
        input = """8
abacbabc"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8
abababab"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
abcde"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """26
codefestivaltwozeroonefive"""
        output = """11"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  S = list(input())
  if N%2:
    print(-1)
    return

  S, T = S[:N//2], S[N//2:]
  N = N//2
  ans = 0
  for i in range(N):
    if S[i] != T[i]:
      ans+=1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()