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
        input = """5 4 2
2 1 1
3 3 4"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4 3
2 1 1
3 3 4
1 4 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 5
1 6 1
4 1 3
6 9 4
9 4 2
3 1 3"""
        output = """64"""
        self.assertIO(input, output)

def resolve():
  # a = 1, 2, 3, 4 をそれぞれ集計すると、白い部分の x の範囲と y の範囲がわかる。
  # x と y の最大最小値をそれぞれ持っておいて、クエリが来る毎に更新していく。
  W, H, N = map(int, input().split(" "))
  x_min = y_min = 0
  x_max = W
  y_max = H
  for i in range(N):
    X, Y, A = map(int, input().split(" "))
    if A == 1: x_min = max(x_min, X)
    if A == 2: x_max = min(x_max, X)
    if A == 3: y_min = max(y_min, Y)
    if A == 4: y_max = min(y_max, Y)
  print(max(x_max-x_min, 0)*max(y_max-y_min, 0))

resolve()

if __name__ == "__main__":
    unittest.main()
