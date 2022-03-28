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
        input = """4 2 3"""
        output = """180"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 987654321 123456789"""
        output = """951633476"""
        self.assertIO(input, output)

def sum_of_star(value):
  if(value&1):
    return int((value+1)/2) * value
  else:
    return int(value/2) * (value+1)


def resolve():
  base = 998244353
  A, B, C= map(int, input().split(" "))
  A_sum = sum_of_star(A)%base
  B_sum = sum_of_star(B)%base
  C_sum = sum_of_star(C)%base
  ans = A_sum*B_sum*C_sum%base

  print(ans)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
