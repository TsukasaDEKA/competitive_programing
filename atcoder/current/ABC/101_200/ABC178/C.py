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
        input = """2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """869121"""
        output = """2511445"""
        self.assertIO(input, output)
    def test_Sample_Input_4(self):
        input = """3"""
        output = """54"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  base = 10**9+7

  if N == 1:
    print(0)
    return True

  ten = pow(10, N, base)
  nine = pow(9, N, base) * 2
  eight = pow(8, N, base)

  print((ten - nine + eight)%base)

if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
