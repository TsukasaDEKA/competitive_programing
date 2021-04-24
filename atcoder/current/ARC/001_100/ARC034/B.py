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

    def test_入力例1(self):
        input = """8"""
        output = """1
4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """101"""
        output = """2
91
100"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """108"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """19"""
        output = """1
14"""
        self.assertIO(input, output)

def resolve():
  # N <= 10**18 で結構大きい。
  # f(x) の最大値は N の桁数 * 9なので、最大で 153 程度。x 部分が支配的。
  # 探索していけそう。
  N = int(input())
  ans = set()
  for tar in reversed(range(max(N-200, 0), N)):
    temp = n = tar
    while n:
      temp+=n%10
      n//=10
    if temp == N:
      ans.add(tar)
  ans = sorted(list(ans))
  print(len(ans))
  if len(ans): print(*ans, sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
