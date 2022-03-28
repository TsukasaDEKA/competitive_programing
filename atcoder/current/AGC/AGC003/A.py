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
        input = """SENW"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """NSNNSNSN"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """NNEW"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """W"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  S = set(list(input()))
  if "N" in S and "S" not in S:
    print("No")
    return
  if "S" in S and "N" not in S:
    print("No")
    return
  if "W" in S and "E" not in S:
    print("No")
    return
  if "E" in S and "W" not in S:
    print("No")
    return

  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()