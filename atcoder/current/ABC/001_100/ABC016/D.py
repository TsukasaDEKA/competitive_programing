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
        input = """-2 0 2 0
4
1 1
-1 1
-1 -1
1 -1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """-3 1 3 1
8
2 2
1 2
1 0
-1 0
-1 2
-2 2
-2 -1
2 -1"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 座標の大小関係が定まっていないけどいつもの判定方法で大丈夫？
  # 線分の交差判定 => https://www.st-hakky-blog.com/entry/2018/09/05/012837
  # 切断される線分の本数/2 + 1 が答え
  def intersect(a, b):
    # 線分 a を直線として扱った時
    ta1 = (a[0][0] - a[1][0]) * (b[0][1] - a[0][1]) + (a[0][1] - a[1][1]) * (a[0][0] - b[0][0])
    ta2 = (a[0][0] - a[1][0]) * (b[1][1] - a[0][1]) + (a[0][1] - a[1][1]) * (a[0][0] - b[1][0])

    # 線分 b を直線として扱った時
    tb1 = (b[0][0] - b[1][0]) * (a[0][1] - b[0][1]) + (b[0][1] - b[1][1]) * (b[0][0] - a[0][0])
    tb2 = (b[0][0] - b[1][0]) * (a[1][1] - b[0][1]) + (b[0][1] - b[1][1]) * (b[0][0] - a[1][0])

    # それぞれ符号が逆(==直線の左右にそれぞれ端点が存在する)かどうかを判定
    return ta1*ta2<0 and tb1*tb2<0

  A_x, A_y, B_x, B_y = map(int, input().split(" "))
  A = [A_x, A_y]
  B = [B_x, B_y]

  N = int(input())
  POINTS = [list(map(int, input().split(" "))) for _ in range(N)]
  count = 0

  for i in range(N):
    if intersect([A, B], [POINTS[i-1], POINTS[i]]):
      count+=1
  print(count//2+1)

resolve()


if __name__ == "__main__":
    unittest.main()
