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
        input = """3 14"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 123"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100000 1000000000"""
        output = """10000"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """31623 1000000000"""
        output = """31250"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  # 2 ~ sqrt(M) まで割っていって、N 以上かつ M を割り切れる値の最小を A とすると M//A が答え。
  # 2 ~ sqrt(M) まで割っていって、割り切れる値がない (M が素数) 場合、1 が答え
  # sqrt(M) <= 31623 なので間に合いそう。
  if N==1:
    print(M)
    return

  A = M
  for i in range(2, int(-(-M**0.5//1))+1):
    if M%i==0: 
      if i >= N:
        A = min(A, i)
      elif M//i >= N:
        A = min(A, M//i)

  print(M//A)

resolve()


if __name__ == "__main__":
    unittest.main()
