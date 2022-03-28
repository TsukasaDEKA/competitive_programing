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
        input = """CODEFESTIVAL"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """FESTIVALCODE"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """CF"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """FCF"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  for i in range(len(S)-1):
    if S[i] == "C":
      for s in S[i:]:
        if s == "F":
          print("Yes")
          return
      else:
        print("No")
      return

  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()