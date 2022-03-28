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
        input = """229 390"""
        output = """Hard"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """123456789 9876543210"""
        output = """Easy"""
        self.assertIO(input, output)

def resolve():
  A, B = map(int, input().split(" "))

  for i in range(19):
    a = A%10
    b = B%10
    if a+b >= 10:
      print("Hard")
      return
    A//=10
    B//=10
  print("Easy")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()