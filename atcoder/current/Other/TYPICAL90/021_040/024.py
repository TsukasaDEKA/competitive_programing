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
        input = """2 5
1 3
2 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
7 8 9
7 8 9"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 999999999
3 1 4 1 5 9 2
1 2 3 4 5 6 7"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  # 差を集計する。
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  sum_ = 0
  for a, b in zip(A, B):
    sum_ += abs(a-b)
  print("Yes" if (sum_ <= K and (K-sum_)%2==0) else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
