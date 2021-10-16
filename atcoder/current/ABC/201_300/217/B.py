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
        input = """ARC
AGC
AHC"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """AGC
ABC
ARC"""
        output = """AHC"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  ans = set()
  ans.add("ABC")
  ans.add("ARC")
  ans.add("AGC")
  ans.add("AHC")
  for i in range(3):
    S = input()
    ans.remove(S)

  print(list(ans)[0])


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()