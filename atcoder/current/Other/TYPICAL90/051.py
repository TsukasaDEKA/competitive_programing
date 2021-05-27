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
        input = """5 2 10
3 8 7 5 11"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1 10
7 7 7 7 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """40 20 100
1 3 1 3 4 1 3 5 5 3 3 4 1 5 4 4 3 1 3 4 1 3 2 4 4 1 5 2 5 3 1 3 3 3 5 5 5 2 3 5"""
        output = """137846528820"""
        self.assertIO(input, output)

def resolve():
  # bit DP かなー
  # N, K が小さい。
  # 40C20 = 137,846,528,820	なので、全探索は厳しい。
  # DFS で途中でPを超えたら打ち切るとかするか。
  # 大きい方から取ってって、P を超過しなかったら全組み合わせでいける。

  N, K, P = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
