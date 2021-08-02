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
        input = """2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2021 617"""
        output = """53731843"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  N, K = map(int, input().split(" "))
  ans = K
  if N > 1:
    ans*=(K-1)*pow(K-2, N-2, mod)
  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
