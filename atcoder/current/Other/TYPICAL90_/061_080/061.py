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
        input = """6
1 2
1 1
2 3
3 1
3 2
3 3"""
        output = """1
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
2 1
3 1
2 2
3 1
2 3
3 1"""
        output = """1
1
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 1000000000
2 200000000
1 30000000
2 4000000
1 500000
3 3"""
        output = """1000000000"""
        self.assertIO(input, output)


def resolve():
  # list の先頭追加は O(n) かかるので間に合わない。
  # deque はランダムアクセスが遅いので間に合わない。
  # list を二つ使って、インデックスを良い感じに使うことで高速に解ける。
  Q = int(input())

  pile = []
  for _ in range(Q):
    t, x = map(int, input().split(" "))
    if t == 1: pile.insert(0, x)
    elif t == 2: pile.append(x)
    else: print(pile[x-1])
  # up = []
  # down = []
  # for _ in range(Q):
  #   t, x = map(int, input().split(" "))
  #   if t == 1: up.append(x)
  #   elif t == 2: down.append(x)
  #   else:
  #     print(up[-x] if len(up) >= x else down[x-len(up)-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
