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
        input = """3 2
RPS"""
        output = """P"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """11 1
RPSSPRSPPRS"""
        output = """P"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 100
S"""
        output = """S"""
        self.assertIO(input, output)

def winner(x, y):
  # アイコ
  if x == y: return x
  # x が勝つ
  if x == "R" and y == "S": return x
  if x == "P" and y == "R": return x
  if x == "S" and y == "P": return x
  return y

def resolve():
  # S を 2 倍 => S[i], S[i+1] (i=0, 2, 4, 6,・・・) の勝った方を残すというのを繰り返す。
  N, K = map(int, input().split(" "))
  S = list(input())
  for k in range(K):
    # S を二倍
    S+=S
    tempS = [""]*N
    for i in range(0, 2*N, 2):
      tempS[i//2] = winner(S[i], S[i+1])
    S=tempS
  print(S[0])
resolve()

if __name__ == "__main__":
    unittest.main()
