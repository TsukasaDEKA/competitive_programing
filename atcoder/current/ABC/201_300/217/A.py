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
        input = """abc atcoder"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """arc agc"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """a aa"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S, T = input().split(" ")


  print("Yes" if S < T else "No")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()