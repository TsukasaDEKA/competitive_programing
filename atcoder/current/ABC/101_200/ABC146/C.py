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
        input = """10 7 100"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1 100000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000 1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1234 56789 314159265"""
        output = """254309"""
        self.assertIO(input, output)

def resolve():
  # A*N + B*d(N) <= X
  # N<= (X - B*d(N))/A
  # 9 <= (100-7*1)/10 = 93/10 = 9.3
  # d(N) = 1,2,3・・・ と順位やっていって最大値を求める。
  A, B, X = map(int, input().split(" "))
  ans = 0
  for d_X in range(1, 11):
    limit = min(10**d_X-1, 10**9)
    ans = max(ans, min((X - B*d_X)//A, limit))

  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
