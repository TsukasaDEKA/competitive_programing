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
        input = """3 2
100 50 200"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 8
50 30 40 10 20"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 100
7 10 4 5 9 3 6 8 2 1"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  # 高橋くん的には買う回数は一回、売る回数も一回が良さそう。
  # 右から見ていって、その地点まで見た時の最大値を記録しながら進む。
  # 街を遡る毎に最大値 - Ai を計算して、それが現在の最大利益を上回った場合は count = 1 する。
  # 最大利益が等しい場合は count += 1 する。
  # これって T 関係ある？問題を理解していないような気がする。
  N, T = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  max_A = 0
  max_gain = 0
  count = 0
  for i in reversed(range(N)):
    max_A = max(max_A, A[i])
    if max_A - A[i] == max_gain:
      count+=1
      continue
    if max_A - A[i] > max_gain:
      max_gain = max_A - A[i]
      count = 1
  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
