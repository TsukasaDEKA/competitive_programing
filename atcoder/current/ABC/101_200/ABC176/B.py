import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """123456789"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """0"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31415926535897932384626433832795028841971693993751058209749445923078164062862089986280"""
        output = """No"""
        self.assertIO(input, output)

from math import ceil, floor

def resolve():
  N = [int(x) for x in list(input())]

  result = 0
  for n in N:
    result += n 
    if result >= 9:
      result %= 9
  print("Yes" if result%9==0 else "No")

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
