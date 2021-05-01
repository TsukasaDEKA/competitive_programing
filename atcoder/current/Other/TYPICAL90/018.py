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
        input = """4
2 1 1
4
0
1
2
3"""
        output = """0.000000000000
24.094842552111
54.735610317245
45.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5121
312000000 4123 3314
6
123
12
445
4114
42
1233"""
        output = """4.322765775902
0.421184234768
15.640867693969
35.396039162484
1.475665637902
43.338582976959"""
        self.assertIO(input, output)

def resolve():
  from math import sqrt, atan2, degrees, sin, cos, pi

  # 桁数が多いのが難
  T = int(input())
  L, X, Y = map(int, input().split(" "))
  Q = int(input())
  takahashi = [X, Y, 0]
  for _ in range(Q):
    E = int(input())
    # 回転
    r = 2*pi*(E%T)/T
    ans = 90-degrees(atan2(sqrt((2*X)**2 + (2*Y+L*sin(r))**2), L*(1-cos(r))))
    # print(T, E, L, kanransha, r)
    print(ans)

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
