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
        input = """1 2 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """13 1 4 3000"""
        output = """87058"""
        self.assertIO(input, output)

def resolve():
  # r*R + g*G + b*B = N を満たす (r, g, b) の組み合わせの個数。
  # 1, 1, 1, 3000 とかが最悪？
  R, G, B, N = map(int, input().split(" "))

  for i in range(R):

  print()

# resolve()

if __name__ == "__main__":
    unittest.main()
