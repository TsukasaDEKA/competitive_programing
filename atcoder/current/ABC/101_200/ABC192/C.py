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
        input = """314 2"""
        output = """693"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6174 100000"""
        output = """6174"""
        self.assertIO(input, output)

def resolve():
  # K 回計算して間に合うか？
  N, K = map(int, input().split(" "))

  for _ in range(K):
    strN = sorted(list(str(N)))
    g1 = int("".join(reversed(strN)))
    g2 = int("".join(strN))
    N = g1 - g2
  print(N)

# resolve()

if __name__ == "__main__":
    unittest.main()
