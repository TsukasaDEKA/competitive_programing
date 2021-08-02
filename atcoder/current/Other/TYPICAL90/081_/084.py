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
ooxo"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
oxoxo"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
ooooo"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7
xxoooxx"""
        output = """16"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 包除原理かな？
  # 全組合せ数 - 連続した o or x で作れる組み合わせの数
  N = int(input())
  S = list(input())
  ans = N*(N-1)//2
  current_char = S[0]
  count = 1
  i = 0
  while i < N-1:
    i+=1
    if S[i] == current_char:
      count+=1
    else:
      current_char = S[i]
      ans -= count*(count-1)//2
      count = 1
  ans -= count*(count-1)//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()