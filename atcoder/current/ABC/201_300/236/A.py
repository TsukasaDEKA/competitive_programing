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
        input = """chokudai
3 5"""
        output = """chukodai"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """aa
1 2"""
        output = """aa"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """aaaabbbb
1 8"""
        output = """baaabbba"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = list(input())

  A, B =[int(x)-1 for x in input().split(" ")]
  S[A], S[B] = S[B], S[A]

  print("".join(S))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()