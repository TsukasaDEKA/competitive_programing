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
        input = """125"""
        output = """176"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9999999999"""
        output = """12656242944"""
        self.assertIO(input, output)

def resolve():
  # S=123 だとして、これは 1*10**0*(23 で作れる式のパターン数) + 1*10**1*(3だけで作れる式のパターン数(1パターン)) + 10*10**2*(何も使わないで作れる式のパターン数(1パターン))・・・
  # のような足し算をしていけば良い。
  S = [int(x) for x in list(input())]
  lenS=len(S)

  ans = 0
  for i in range(lenS):
    # i 桁目を含まない、i より左と右の桁数
    left_pattern = 2**i
    right_digits = lenS-1-i
    for right_length in range(right_digits+1):
      base = S[i]*10**right_length
      ans += base*left_pattern*2**(max(right_digits-right_length-1, 0))

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
