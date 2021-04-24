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

    def test_Sample_Input_1(self):
        input = """4
2 3 5
2 1 5
1 2 5
3 2 5"""
        output = """2 2 6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
0 0 100
1 1 98"""
        output = """0 0 100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
99 1 191
100 1 192
99 0 192"""
        output = """100 0 193"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
32 67 0
32 68 1
33 68 0
31 68 0
32 69 0"""
        output = """32 68 1"""
        self.assertIO(input, output)


def resolve():
  from collections import deque
  inf = 10**10+1
  N = int(input())
  points = [[int(x) for x in input().split(" ")] for _ in range(N)]
  # Cx と Cy が 0 ~ 100 の整数である点に着目する。
  # 2 点を取って、Hi+ abs(Xi-Cx) + abs(Yi-Cy) == Hj+ abs(Xj-Cx) + abs(Yj-Cy) が成り立つ Cx, Cy を全探索すると、
  # Cx, Cy の組みが複数残る筈なので、別の 2 点を取って同じ様に成り立つか確認していく。
  # 最終的に候補が一つ残る筈なので、それを使って H を求める。
  # ~~任意の i に対して H = Hi+ abs(Xi-Cx) + abs(Yi-Cy) が成り立つ。~~
  # 成り立たない。正しくは Hi > 0 の時、H = Hi+ abs(Xi-Cx) + abs(Yi-Cy) が成り立つ
  none_hight_point = None
  for Xi, Yi, Hi in points:
    if Hi != 0:
      none_hight_point = (Xi, Yi, Hi)
      break

  # 全探索してみる。
  for Cx in range(100+1):
    for Cy in range(100+1):
      Xi, Yi, Hi = none_hight_point
      H = Hi+ abs(Xi-Cx) + abs(Yi-Cy)
      # もし全ての点に対して矛盾しなければ答え。
      is_ans = True
      for point in points:
        Xi, Yi, Hi = point
        if Hi != max(H - abs(Xi-Cx) - abs(Yi-Cy), 0):
          is_ans = False
          break
      if is_ans:
        print(Cx, Cy, H)
        return

resolve()

if __name__ == "__main__":
    unittest.main()
