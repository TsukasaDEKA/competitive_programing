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

    # def test_Sample_Input_1(self):
    #     input = """10"""
    #     output = """5"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """1111111111111111111"""
    #     output = """162261460"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """110"""
    #     output = """19"""
    #     self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """111011011"""
        output = """15219"""
        self.assertIO(input, output)

import sys
sys.setrecursionlimit(500*500)

def resolve():
  mod = 10**9+7

  S = [int(x) for x in list(input())]
  N = len(S)

  def f(index):
    # print(*S[index:], sep="")
    if index == N: return 1
    if S[index] == 0: return f(index+1)%mod
    return (pow(3, N-index-1, mod) + (2*f(index+1))%mod) % mod

  print(f(0))

if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()