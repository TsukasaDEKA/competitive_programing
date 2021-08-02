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
        input = """13579
10000 20000"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12345678901234567890
0 1000000000"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """05
5 5"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """0
0 1"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = list(input())
  L, R = map(int, input().split(" "))
  if S[0] == "0" and len(S) > 1:
    print("No")
    return
  S = int("".join(S))
  if S < L or S > R: 
    print("No")
    return


  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()