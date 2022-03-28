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
        input = """X Y Z"""
        output = """X,Y,Z"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """A  B, C"""
        output = """A,B,,C"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """QWERTY"""
        output = """QWERTY"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = list(input())
  N = len(S)
  ans = []
  i = 0
  while i < N:
    if S[i] == " ":
      while S[i] == " ":
        i+=1
      ans.append(",")
    else:
      ans.append(S[i])
      i+=1

  print("".join(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()