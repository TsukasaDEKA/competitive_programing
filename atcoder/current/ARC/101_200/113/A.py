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
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10"""
        output = """53"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31415"""
        output = """1937281"""
        self.assertIO(input, output)

def resolve():
  # A を固定して、BC < K//A となる B, C を求める。
  # 次に B を固定して、
  K = int(input())
  ans = 0
  for a in range(1, K+1):
    for b in range(1, K//a+1):
      C = K//(a*b)
      ans+=C
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
