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
        input = """4 20 2 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1000000000000000000 10 1000000000"""
        output = """1000000007"""
        self.assertIO(input, output)

def resolve():
  X, Y, A, B = map(int, input().split(" "))

  strength = X

  p = 0
  inclease_val = strength * (A - 1)
  while inclease_val < B and strength + inclease_val < Y:
    strength += inclease_val
    inclease_val = strength * (A - 1)
    p += 1

  q = (Y - strength - 1) // B
  print(p + q)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
