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
        input = """xoxxoxxo"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """xxoxxoxo"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """ox"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """oo"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = [1 if x == "o" else 0 for x in list(input())]
  N = len(S)

  if N <= 2:
    if S == [1, 1]: print("No")
    else: print("Yes")
    return


  for i in range(N-2):
    if sum(S[i:i+3]) != 1:
      print("No")
      return

  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()