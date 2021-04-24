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
        input = """12"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """13"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """17"""
        output = """4368"""
        self.assertIO(input, output)
    def test_Sample_Input_4(self):
        input = """200"""
        output = """4368"""
        self.assertIO(input, output)


def resolve():
  from scipy.special import comb
  L = int(input())
  print(int(comb(L-1, 11, exact=True)))

# resolve()

if __name__ == "__main__":
    unittest.main()
