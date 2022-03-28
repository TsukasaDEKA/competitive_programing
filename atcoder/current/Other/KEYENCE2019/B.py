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
        input = """keyofscience"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """mpyszsbznf"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """ashlfyha"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """keyence"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """kyeeeence"""
        output = """NO"""
        self.assertIO(input, output)
def resolve():
  S = input()
  N = len(S)
  for l in range(N):
    for r in range(N):
      if "".join(S[:l]+S[r:]) == "keyence":
        print("YES")
        return
  print("NO")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()