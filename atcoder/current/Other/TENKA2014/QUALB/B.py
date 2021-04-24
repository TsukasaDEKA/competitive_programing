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

    def test_入力例1(self):
        input = """3
eternalstaticfinal
eternal
static
final"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
eternalstaticfinal
eternal
static
final
fin
al"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5
abcdef
abc
def
abcdef
d
ef"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """5
aaaa
a
aa
aaa
aaaa
b"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """10
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaaaaaa
aaaaaaaa
aaaaaaaaa
aaaaaaaaaa"""
        output = """146491918"""
        self.assertIO(input, output)

def resolve():
  # |S| <= 1000 程度なので 二乗オーダー程度なら通せる。
  # N <= 100 
  # i, j (i < j) を定義して、全ての i~j の区間でなんかいい感じに出来そう。
  # それを使ってどうするか、だけど全然思いつかない。
  # dp[i] = i 文字目まで使った時に何パターンで表現できるかって出来ないか
  # 例えば文字の間に仕切りを入れると考えてみる。
  # 1000文字の間に仕切りを入れる方法は、2**(1000-1) パターンある。
  # 全部探索してると間に合わなさそう。どこかで計算の省略をしたい。
  # 例 4 の場合で i ~ j の二次元で作成してみる。

  # 例 3 だと以下のような感じになる。
  # [0, 0, 1, 0, 0, 1]
  # [0, 0, 0, 0, 0, 0]
  # [0, 0, 0, 0, 0, 0]
  # [0, 0, 0, 1, 0, 1]
  # [0, 0, 0, 0, 0, 1]
  # [0, 0, 0, 0, 0, 0]
  # 右端のマスからBFS出来そう。
  # i == 0 にたどり着けるか判定すれば良くて、
  # (4, 5)=>(3, 3)=>(0, 2)
  # (3, 5)=>(0, 2)
  # (0, 5)
  # の 3 通りの経路がある。
  # 例 4 だと以下のような感じになる。
  # [1, 1, 1, 1]
  # [0, 1, 1, 1]
  # [0, 0, 1, 1]
  # [0, 0, 0, 1]
  # グラフの問題に落とし込めそう。
  # 1 行目から計算していった方が楽か。
  # 一見計算量が爆発的に増えそうだけど、N が最大 100 なので、
  # 最悪のケースでも 幅 100 程度の対角に伸びる帯状になって、そこまで計算量は上がらないはず。
  # 下の行からいい感じに足し算していくと間にあう・・・？
  # BFS だと厳しいかもしれない。
  # 例 3
  # [4, 2, 1, 1] => 4+2+1+1 = 8
  # [0, 2, 1, 1]
  # [0, 0, 1, 1]
  # [0, 0, 0, 1]


  mod = 1000000007
  N = int(input())
  S = input()
  T = set([input() for _ in range(N)])

  is_in = [[0]*(len(S)+1) for _ in range(len(S))]
  for i in range(len(S)):
    for j in range(i+1, len(S)+1):
      # 半開区間で考える。
      is_in[i][j] = 1 if S[i:j] in T else 0
  print(*is_in, sep="\n")
  # # 足し算と更新を繰り返していくっぽいがよくわからん
  # sum_row = [0]*len(S)
  # sum_row[-1] = is_in[-1][-1]
  # for i in reversed(range(len(S)-1)):
  #   for j in reversed(range(i, len(S))):
  #     if j+1 == len(S):
  #       sum_row[i] += is_in[i][j]
  #     else:
  #       sum_row[i] += is_in[i][j]*sum_row[j+1]
  #     if sum_row[i] > mod: sum_row[i]%=mod
  # print(sum_row[0]%mod)
# resolve()

if __name__ == "__main__":
    unittest.main()
