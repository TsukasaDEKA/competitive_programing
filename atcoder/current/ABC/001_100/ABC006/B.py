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

    def test_入力例_1(self):
        input = """7"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000"""
        output = """7927"""
        self.assertIO(input, output)

def resolve():
  # トリボナッチ数列の100 番目の値は 98079530178586034536500564 でとても大きい。
  # 逐次 mod を取っていけばいけそう。
  mod = 10007
  N = int(input())
  ans = [0]*N
  if N <= 2:
    print(0)
    return
  ans[2] = 1
  for i in range(3, N):
    ans[i] = sum(ans[i-3:i])
    if ans[i] >= mod: ans[i]%=mod
  print(ans[-1])

resolve()

if __name__ == "__main__":
    unittest.main()
