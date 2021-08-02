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
        input = """3
0 0
0 1
1 0
2 0
3 0
3 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 0
1 1
3 0
-1 0
-1 1
-3 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
0 0
2 9
10 -2
-6 -7
0 0
2 9
10 -2
-6 -7"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
10 5
-9 3
1 -5
-6 -5
6 9
-9 0
-7 -10
-10 -5
5 4
9 0
0 -10
-10 -2"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  # ABCD が 10 以下
  # N が 100 以下
  # この範囲なら 90 度以外の移動はない。
  # ある点からの相対座標を回転させてやれば？
  # B の特定の点を取って、そこと A のある点を取って、そこ中心に回転させる動作を行う。

  from math import sin, cos, pi
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  B = [[int(x) for x in input().split(" ")] for _ in range(N)]
  base_x, base_y = B[0]
  set_B = set()
  for i in range(N):
    x, y = B[i]
    set_B.add((x, y))

  for i in range(360+1):
    phi = pi*i/180
    rotate_x = [cos(phi), -sin(phi)]
    rotate_y = [sin(phi), cos(phi)]
    # 回転中心になる A を選ぶ
    for j in range(N):
      x, y = A[j]
      # 回転
      x, y = rotate_x[0]*x + rotate_x[1]*y, rotate_y[0]*x + rotate_y[1]*y

      # 平行移動
      diff_x, diff_y = base_x-x, base_y-y
      # 全部同じ変換をする。
      for k in range(N):
        x_k, y_k = A[k]
        # 回転
        x_k, y_k = rotate_x[0]*x_k + rotate_x[1]*y_k, rotate_y[0]*x_k + rotate_y[1]*y_k

        # 平行移動
        x_k += diff_x
        y_k += diff_y
        
        # 精度の問題で上手くマッチしない場合は計算を切り上げる。
        if abs(x_k-round(x_k)) > 0.05 or abs(y_k-round(y_k)) > 0.05: break
        # 精度の問題で上手くマッチしない場合は計算を切り上げる。
        if (round(x_k), round(y_k)) not in set_B: break
      else:
        print("Yes")
        return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()