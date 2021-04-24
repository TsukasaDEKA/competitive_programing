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
        input = """2 3 9"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3 10"""
        output = """Yes"""
        self.assertIO(input, output)

from decimal import Decimal

def sqrt(a):
  return a**Decimal("0.5")

def resolve():
  A, B, C = map(Decimal, input().split(" "))
  print("Yes" if sqrt(A)+sqrt(B) < sqrt(C) else "No")

resolve()

if __name__ == "__main__":
    unittest.main()
