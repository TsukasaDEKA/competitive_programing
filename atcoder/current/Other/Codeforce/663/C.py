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
        input = """4"""
        output = """16"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """583291"""
        output = """135712853"""
        self.assertIO(input, output)

def resolve():
  N = int(input())

  base = 10**9 + 7
  mod_1 = 2
  for i in range(3, N + 1):
    mod_1 *= i
    if mod_1 > base:
      mod_1 = mod_1 % base

  mod_2 = pow(2, N-2, base)

  result = (mod_1 - 2 * mod_2) % base
  print(result)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
  unittest.main()