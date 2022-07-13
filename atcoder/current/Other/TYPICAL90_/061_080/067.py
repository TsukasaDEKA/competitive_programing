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
        input = """21 1"""
        output = """15"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1330 1"""
        output = """555"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2311640221315 15"""
        output = """474547"""
        self.assertIO(input, output)

def resolve():
  # N は 8 進数で最大 21 桁
  N, K = input().split(" ")
  if int(N) <= 7:
    print(N)
    return
  K = int(K)
  for _ in range(K):
    N = int(N, 8)
    nonary = ""
    while N != 0:
      s = str(N%9)
      nonary += s if s!="8" else "5"
      N//=9
    N = nonary[::-1]
  print(N)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
