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

    def test_入力例1(self):
        input = """7 3
...o.o."""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """8 4
...o.ooo"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 4
oooo"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """6 2
......"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """4 3
...o"""
        output = """1"""
        self.assertIO(input, output)
def resolve():
  # 一番右側にある . を探せば、移動距離が決まるので、あとは何発打てば良いか決めるだけになる。
  # 右から順に見ていって、 . を見つけたら打つ回数を 1 追加して R 分だけ移動 (移動後 0 以下になる時は 0 まで移動)を繰り返す。
  N, R = map(int, input().split(" "))
  S = list(input())
  ans = 0

  i = N-1
  while S[i] == "o":
    i-=1
    if i < 0:
      print(0)
      return

  i -= R
  # 移動部分はここで処理
  ans = max(i+1, 0) + 1

  while i >= 0:
    if S[i] == "o":
      i -= 1
    else:
      ans += 1
      i -= R
    if i < 0:
      break

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
