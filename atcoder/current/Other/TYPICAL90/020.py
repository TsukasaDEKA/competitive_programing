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
        input = """4 3 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """16 3 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 3 2"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  # loga < blogc かどうかを判定。
  # log の誤差が怖いので、a < c**b を計算する。
  # b, c の制約が小さいので間に合いそう。
  A, B, C = map(int, input().split(" "))
  print("Yes" if A < pow(C, B) else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
