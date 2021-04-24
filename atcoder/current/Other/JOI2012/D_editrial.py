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
        input = """5 3
3 1
1 1
4 2"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 5
10 2
4 3
12 1
13 2
9 1"""
        output = """2640"""
        self.assertIO(input, output)

def resolve():
  # 連続した前後の予定を見て、何通りのパスタを選べるか考える。
  # 0 : 未選択の日と考えて、[1, 0, 0] の場合、
  # [1, 1, 2], [1, 1, 3]
  # [1, 2, 1], [1, 2, 2], [1, 2, 3]
  # [1, 3, 1], [1, 3, 2], [1, 3, 3]
  # 以上の 3 種類が考えられる。
  # 意外とむずい。
  # 一次元配列だとダメそう。日付*パスタの種類の二次元配列？

  # 解説を見ると、「i+1 日目の予定を決めるためには、i 日目と i–1 日目の予定が影響する」

  N, K = map(int, input().split(" "))
  C = [-1]*N
  for i in range(K):
    A, B = map(int, input().split(" "))
    C[A-1] = B

  dp = [[[0]*3 for _ in range(3)] for _ in range(N)]
  print()

# resolve()

if __name__ == "__main__":
    unittest.main()
