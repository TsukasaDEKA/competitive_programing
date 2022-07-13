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
        input = """2
-1 2
1 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 0
0 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
2 5
2 5
-3 4
-4 -8
6 -2"""
        output = """35"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
1000000000 1000000000
-1000000000 1000000000
-1000000000 -1000000000
1000000000 -1000000000"""
        output = """8000000000"""
        self.assertIO(input, output)

def resolve():
  # x と y を独立に考えることができる。
  # それぞれの中央値 (N が偶数の場合は真ん中の 2 つの間のどれか好きなやつ) をとってそこに発電所を置くのが最適。

  # -「x と y を独立に考えることができる。」 について
  # 発電所の場所を仮に (x_ans, y_ans) と置く。
  # 発電所と工場 i の不便さ = |x_i - x_ans| + |y_i - x_ans| なので、
  # 不便さの総和 = |x_1 - x_ans| + |y_1 - y_ans| + |x_2 - x_ans| + |y_2 - y_ans| + ・・・ + |y_n - y_ans| + |x_n - x_ans|
  # これを x_ans と y_ans に着目して並び替えると 
  # 不便さの総和 = (|x_1 - x_ans| + |x_2 - x_ans| + ・・・ +  |x_n - x_ans|) + (|y_1 - y_ans| + |y_2 - y_ans| + ・・・ + |y_n - y_ans|) となる。
  # この式は x_ans の値をいくら変更しても |y_i - y_ans| の値に影響は与えないし、
  # y_ans の値をいくら変更しても |x_i - x_ans| の値に影響を与えない。
  # つまり、x_ans と y_ans を独立に考えることができる。

  # - 「それぞれの中央値 (N が偶数の場合は真ん中の 2 つの間のどれか好きなやつ) をとってそこに発電所を置くのが最適。」 について
  # 発電所の位置を仮に (x_ans, y_ans) と置いて、
  # x_ans を増やしたり減らしたりした時に、不便さ sum(|x_i - x_ans|) (i = [1, N]) がどれくらい変化するかを考える。
  # x_ans' = x_ans - 1 と置くと、
  # |x_i - x_ans'| = |x_i - (x_ans - 1)| = |x_i - x_ans + 1| = |(x_i - x_ans) + 1|
  # ここで、x_i - x_ans >= 0 であれば |(x_i - x_ans) + 1| > |x_i - x_ans| になって不便さが増える。
  # また、x_i - x_ans < 0 であれば |(x_i - x_ans) + 1| < |x_i - x_ans| になって不便さが減る。
  # なので全体の不便さの増減は、p = <x_i >= x_ans である x_i の個数>、q = <x_i < x_ans である x_i の個数> と置くと p-q となる。
  # つまり、 p < q である時に x_ans -= 1 すると不便さが減る。
  # N が奇数の時、x_ans を中央値+1 において、x_ans -= 1 することを考える。この時点で p < q であるので不便さは減る。
  # そこからさらに x_ans -= 1 しようとすると、今度は p > q となってるので不便さは増える。
  # 例: x = [1, 3, 5, 7, 9]、 の時、x_ans が 6 なら p < q で x_ans が 5 なら p > q になる。
  # N が偶数の場合、 x_ans が中央の数字 2 つを小さい順から c_min, c_max と置くと
  # c_max < x_ans の時 p < q、c_min < x_ans <=c_max の時 p == q、x_ans <= c_min の時 p > q になる。
  # 例: x = [1, 3, 5, 7, 9, 11] の時、x_ans = 8 なら p < q、 x_ans = 6, 7 なら p == q、 x_ans = 5 なら p > q になる。
  # 今回は不便さを最小にしたいので、p < q であるなら x_ans -= 1 をして、そうでないならやらない、とすると
  # x_ans の最適な値は中央値 (N が偶数の場合は真ん中の 2 つの数字の間のどれか好きなやつ) になる事がわかる。
  # y_ans も同様である。
  N = int(input())
  X_Y = [[int(x) for x in input().split(" ")] for _ in range(N)]

  # それぞれソートしておく
  X = sorted([x[0] for x in X_Y])
  Y = sorted([x[1] for x in X_Y])

  # 発電所の場所を決める
  ans_x = X[N//2]
  ans_y = Y[N//2]

  # 不便さを計算する
  ans = sum(abs(x-ans_x)+abs(y-ans_y) for x, y in zip(X, Y))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
