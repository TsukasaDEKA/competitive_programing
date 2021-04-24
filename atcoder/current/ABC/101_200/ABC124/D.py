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
        input = """5 1
00010"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """14 2
11101010110011"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1
1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 似た問題最近といた気がする。
  # https://atcoder.jp/contests/abc140/tasks/abc140_d
  # abc140_d とこの問題の違いはカウントの仕方。
  # 与えられる S を 0 の塊と 1 の塊の組み合わせと捉える。
  # 0 の塊の内、K 個を反転させて 1 にすることができる。
  # 1 を挟んで隣あう 0 の塊の内、どの 0 の塊を反転させるか？という問題。
  # 0 の塊と 1 の塊の累積和をそれぞれ取って、K 個の 1 を挟んで連続した 0 の塊に含まれる 0 の個数 + その間の 1 の個数 + 0 の両端に隣接している 1 の塊に含まれる 1 の個数を求める。

  # ちなみに複数の 0 と 1 のまとまりを選択するのと一個づつ選択するのは等価。
  # K=2 で 11101110111 を反転させる時、
  # 01110を反転させて 11101110111 => 11110001111 => 11111111111 とするのと、
  # 0 を反転させて 11101110111 => 11111110111 => 11111111111 とするのは回数も結果も同じ。
  N, K = map(int, input().split(" "))
  S = [int(x) for x in list(input())]

  one_blocks = []
  zero_blocks = []
  # zero_blocks[i] が one_blocks[i]の一つ前の 0 の塊というようにするために調節する。
  if S[0]==1: zero_blocks.append(0)
  i=0
  while True:
    one_count = 0
    if i>=N: break
    while S[i]==1:
      one_count+=1
      i+=1
      if i>=N: break
    one_blocks.append(one_count)

    zero_count=0
    if i>=N: break
    while S[i]==0:
      zero_count+=1
      i+=1
      if i>=N: break
    zero_blocks.append(zero_count)
  # zero_blocks[i] が one_blocks[i]の一つ前の 0 の塊というようにするために調節する。
  if one_blocks[0]==0: one_blocks=one_blocks[1:]

  # zero_blocks の個数が K 以下であれば全て 1 にできるので N を出力
  if len(zero_blocks) <= K or (zero_blocks[0]==0 and len(zero_blocks)-1 <= K):
    print(N)
    return

  # 区間和を取りたいので、累積和を作る。
  integral_one  = [0]*(len(one_blocks)+1)
  for i in range(1, len(integral_one)): integral_one[i] = integral_one[i-1]+one_blocks[i-1]
  integral_zero = [0]*(len(zero_blocks)+1)
  for i in range(1, len(integral_zero)): integral_zero[i] = integral_zero[i-1]+zero_blocks[i-1]

  ans = 0
  for i in range(len(integral_zero)-K):
    sum_zero = integral_zero[i+K]-integral_zero[i]
    one_left = max(0, i-1)
    one_right = min(len(integral_one)-1, i+K)
    sum_one = integral_one[one_right]-integral_one[one_left]
    ans = max(ans, sum_zero+sum_one)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
