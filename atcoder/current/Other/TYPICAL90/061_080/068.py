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
7
0 1 2 3
1 1 2 1
1 3 4 5
0 3 4 6
1 3 4 5
0 2 3 6
1 3 1 5"""
        output = """2
Ambiguous
1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """15
25
0 11 12 41
0 1 2 159
0 14 15 121
0 4 5 245
0 12 13 157
0 9 10 176
0 6 7 170
0 2 3 123
0 7 8 167
0 3 4 159
1 12 11 33
0 10 11 116
0 8 9 161
1 9 12 68
1 12 12 33
1 7 12 74
0 5 6 290
1 8 9 93
0 13 14 127
1 10 12 108
1 14 1 3
1 13 8 124
1 12 11 33
1 12 10 33
1 5 15 194"""
        output = """8
33
33
33
68
33
144
93
8
108
118"""
        self.assertIO(input, output)

def resolve():
  # Q <= 10**5 なので 1 クエリに対して O(1) とか O(logN) くらいで処理したい。
  # 最後まで A の値は一意に定まることは無い。
  # その為、結論を得るまでにいくつかの値を跨ぐ必要がある場合が存在する点に注意する。
  # 例えば A1+A2 = 5, A2+A3 = 4, A3+A4 = 6 の時、 A1 = 2 だと仮定した時の A4 は？と言うクエリが来た時、
  # A2 = 3, A3 = 1, A4 = 5 のように 3 回の計算が必要になる。
  # これを愚直にやると最悪ケースで O(N**2) になって TLE になる。
  # どこかで計算を省略できないかを考える。
  # 例えば、A1+A2 = 5, A2+A3 = 4, A3+A4 = 6 の時、連立方程式を解けば
  # (A1+A2)-(A2+A3) = 5-4 なので A1-A3 = 1、(A1-A3)+(A3+A4) = 1+6 なので A1+A4 = 7 であり、
  # A1 = 2 だと仮定した時の A4 は 5 であると計算できる。
  # 一回の T=1 のクエリを処理した時に、その経路の計算結果を記録しておけば経路上の 2 点間のクエリは O(1) で求められるようになる。
  # 問題はそれをどのように実装するかという点にある。
  # N*N の二次元配列だと最大で 10**10 のデータが必要なので MLE する。
  # 
  # ここまで考えて構造的に Union-Find に似ていることに気が付く。
  # 例えば T = 0 クエリは Axi と Ayi を union する動作で、
  # 上記の連立方程式を解く計算は経路圧縮の動作になる。
  # また、Ambiguous になる条件は、Axi と Ayi の根が別々であることである。
  # 適当な Ai を根と定めて、そこからの差がどの程度なのかを決めておけば良さそう。
  N = int(input())
  Q = int(input())
  for _ in range(N):
    T, X, Y, V = [int(x) for x in input().split(" ")]

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
