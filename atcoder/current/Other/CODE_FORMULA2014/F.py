import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  # 問題だと円だが、その円に外接する正方形で考える。
  # その正方形の面積の和をとると 1353400 になる。1500**2 = 2250000 なので充足率が 6 割程度あればよい。
  # 蛇腹状に並べていけば良い。プログラムを書くのが大変そう。
  # 普通に順に並べていってもいける。
  # 大きい方から並べていっても大丈夫っぽい
  ans = [None for _ in range(101)]
  i = 100
  y = 0
  while i > 0:
    # x 座標は 0 スタート
    x = 0
    # 一列分の y 座標は全部同じにする。
    i_ = i
    y += i
    while x+2*i_ <= 1500:
      x += i_
      ans[i_] = (x, y)
      x += i_
      i_ -= 1
      if i_ <= 0: break
    y += i
    i = i_

  for a in ans[1:]:
    print(*a)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()