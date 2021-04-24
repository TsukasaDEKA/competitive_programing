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
10 12 1 2 14"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 7
-10 -3 0 9 -100 2 17"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 1
-100000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 折り返しをするのは無駄にコストがかかる。
  # ソートした時に、座標同士の間の内、コマの数 - 1 個を選ばなくて済む。
  N, M = map(int, input().split(" "))
  X = sorted([int(x) for x in input().split(" ")])
  ans = 0
  diff_X = [0]*(M-1)
  for i in range(M-1):
    diff_X[i] = X[i+1] - X[i]
    ans += diff_X[i]

  diff_X.sort(reverse=True)
  ans -= sum(diff_X[:N-1])
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
