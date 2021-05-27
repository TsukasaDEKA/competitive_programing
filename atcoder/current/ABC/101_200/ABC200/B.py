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
        input = """2021 4"""
        output = """50531"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """40000 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8691 20"""
        output = """84875488281"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, K = map(int, input().split(" "))

  for i in range(K):
    if N >=200 and N%200 == 0:
      N//=200
    else:
      N = N*1000+200

  print(N)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
