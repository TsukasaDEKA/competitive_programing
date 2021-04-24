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
        input = """BBBWW"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """WWWWWW"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """WBWBWBWBWB"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  # w と b の境界の個数を調べれば良い。
  S = list(input())

  ans=0
  for i in range(len(S)-1):
    if S[i] != S[i+1]: ans+=1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
