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
        input = """2 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 8"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """100000 100000"""
        output = """530123477"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  N, M = map(int, input().split(" "))

  # 差が 1 以上だと並べ方は 0 通りになる。
  if abs(N-M) > 1:
    print(0)
    return

  ans = 1
  for n in range(2, N+1):
    ans*=n
    if ans>mod: ans%=mod
  for m in range(2, M+1):
    ans*=m
    if ans>mod: ans%=mod
  if abs(N-M) == 0: ans*=2

  print(ans%mod)

resolve()

if __name__ == "__main__":
    unittest.main()
