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
10 4 3
1000 11 2
998244353 897581057 595591169
10000 6 14"""
        output = """2
-1
249561088
3571"""
        self.assertIO(input, output)

# 拡張ユークリッドの互除法
def extgcd(a, b):
  if b:
    g, y, x = extgcd(b, a % b)
    y -= (a // b)*x
    return g, x, y
  return a, 1, 0

def resolve():
  T = int(input())
  # オイラーのファイ関数とかしらねぇ！！
  # 拡張ユークリッドの互除法でいけるらしい。extgcd・・・？
  # 玉座の座標を 0 だとする。初期地点は玉座 + S なので、x 回移動した時の座席は (S+K*x)%N になる。
  # (S+K*x)%N == 0 の時、玉座に座れる。その時の最小の x を求める。
  # つまり、
  # S+K*x ≡ 0 (mod N)
  # K*x ≡ -S (mod N)
  # a*x ≡ b (mod N) (a = K, b = -S)
  # (a/b)*x ≡ 1 (mod N)
  # つまり a/b = -K/S の逆元 x を求める。
  # 具体的には、まず K*x ≡ 1 mod N になる x を求め、その両辺に (-S) を掛けると K*x*(-S) ≡ (-S) mod N となるので、
  # 先ほどの x に (-S) を掛けて mod N を取ったものが答え。

  for _ in range(T):
    N, S, K = map(int, input().split(" "))
    SmodN = S%N
    g, x, _ = extgcd(K, N)
    # K, N が互いに素 (g == 1) の場合、全ての席に座ることができる == 玉座に座れる。
    # また、K, N の最大公約数で S が割り切れる場合、(A*K+S) = 0 (mod N) (A は整数) となる A が必ず存在する == 玉座に座れる。
    if S%g != 0:
      print(-1)
      continue
    # K*x ≡ g (mod N) となる x を求めた。欲しいのは K*x ≡ 1 (mod N) となる x なので両辺を g で割る。
    # 両辺に (-S//g) をかけると、K*x*(-S//g) ≡ -S つまり、 x*(-S//g) が答えになる。
    # K//g * x ≡ 1 (mod N//g)
    # 答えは K//g*x' ≡ -S//g (mod N//g) となる x' なので、両辺に -S を掛けて、
    # K*x*(-S) ≡ -S より、x' = (-S)*x
    N//=g
    # S//=g
    # 以下の出力だと x が負の時に答えが間違う場合がある
    # ・・・と思ったけど Python の余り計算だとちゃんと出してくれるのでこれで問題なし。
    # % 計算で負の値が出る言語だと ((x*(-S//g))%N+N)%N しないといけない (この式も間違えてるかも。)
    print((x*(-S//g))%N)

# resolve()

if __name__ == "__main__":
    unittest.main()
