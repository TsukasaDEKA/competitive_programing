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
        input = """3
aba"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
aaaaaaaaaa"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
baaca"""
        output = """17"""
        self.assertIO(input, output)

def resolve():
  # どんな状況になったら操作できないかを考える。
  # 操作の内容が Si = b (c) を一つ選び・・・なので、b, c がなくなった時であることがわかる。
  # b, c がなくなった時というのは全ての文字が a になった時だと考えられる。
  # 文字の遷移が a => b => c => (選ばれた Si に関しては c => b => a) だということを考えると、
  # この 3 文字の関係性は数字のようになっていると予想できる。
  # 仮に a, b, c = 0, 1, 2 とした時、操作を行うとは以下の 2 つを行うことだと考えられる。
  # - Si > 0 である Si に対して -1 (下限 0) する
  # - S0~i に対しては +1 (2 以上なら+1 して %=3)　する
  # Si を選んだ時に、S0 ~ i-1 に 2 が存在している場合、2=>0 となるので操作できる回数が無駄になる。
  # 逆に S0 ~ i-1 に 2 が存在している時はその 2 を先に処理すると操作できる回数を無駄にせずに済む。
  # そう考えるとシンプルに処理できそう。
  # Si を 0, 1, 2 に置き換えた状態で、
  # ans = sum(2**i * Si)(i = 0 ~ N-1) (i は 0-index)

  # -> sum(2**i * Si) になる根拠というかそれに到る思考過程について
  # 各桁の 1 あたりの操作回数 (価値) が知りたい。
  # 上記の考察から左側から順に処理していくことで無駄なく操作を行えることがわかっているので、
  # 左側から順に価値を決めていく。
  # baa => 100 の場合、操作は 1 回だけ行える。なので、i = 0 の桁に入っている数字の価値は 1/1 であると考えられる。
  # aba => 010 は 2 回操作を行える。
  # 具体的には S1 に 1 回操作を行うと i = 0 の桁に入っている数字が +1 つまり価値が 1 上がる。
  # 1 回操作に 1 の価値を足すことになるなので 2/1 の価値になる。
  # aab => 001 の場合を考える。S2 に操作を行うと 110 になり、1+2 の価値が上がる。
  # つまり S2 には 1 回の操作に 1+2 = 3 の価値を足すことになるので合計 4/1 の価値になる。
  # 漸化式っぽいのを書くと、
  # Si の価値 = Si*(1 回の処理 + sum(0 ~ i-1 桁目にある数字 1 個分の価値)) になり、これを i=0 から順に考えていくと
  # Si の価値 = Si*2**i になる。
  # 求めたいのは操作回数の最大値なので、i を 0 ~ N-1 まで動かした時の sum(Si*(2**i)) が答えになる。
  alpha2num = lambda c: ord(c) - ord('a')

  N = int(input())
  # alpha2num で数字に置き換える。
  S = [alpha2num(x) for x in list(input())]
  ans = sum(S[i]*(2**i) for i in range(N))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
