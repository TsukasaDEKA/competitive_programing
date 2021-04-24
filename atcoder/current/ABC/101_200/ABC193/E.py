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
        input = """3
5 2 7 6
1 1 3 1
999999999 1 1000000000 1"""
        output = """20
infinity
1000000000999999999"""
        self.assertIO(input, output)


#     def test_Sample_Input_1(self):
#         input = """1
# 5 2 7 6"""
#         output = """20"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """1
# 999999999 1 1000000000 1"""
#         output = """1000000000999999999"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """1
# 1 1 1 3"""
#         output = """1"""
#         self.assertIO(input, output)


#     def test_Sample_Input_4(self):
#         input = """1
# 1 1 3 1"""
#         output = """infinity"""
#         self.assertIO(input, output)

import sys
sys.setrecursionlimit(500*500)

def resolve():
  # inf の設定はテストケース 3 の答えが 10**18 程度なので 10**30 にしてみたけど足りないかも。
  inf = 10**30+1
  def extgcd(a, b):
    # ax + by = d (d = 最大公約数) とした時、d, x, y を返す。
    if b:
      g, y, x = extgcd(b, a % b)
      y -= (a // b)*x
      return g, x, y
    return a, 1, 0

  from math import gcd
  def crt(b1, m1, b2, m2, d=None, p=None, q=None):
    # x ≡ b1 (mod m1)、x ≡ b2 (mod m2) <=> x ≡ r (mod lcm(m1, m2)) となる x, r を返す。
    # また、解が存在しない時、それを返す。
    if d is None:
      d, p, q = extgcd(m1, m2)
    # 解が存在しない場合。
    if d != 1 and b1%d != b2%d: return -1, -1
    x = b1 + m1*p*(b2-b1)//d
    r = x%((m1*m2)//d)
    return x, r

  T = int(input())
  # 二つの街の間なのでそんなに難しくない気がする。
  # 電車の周期と睡眠周期が重なるかどうかを判定する。
  # 電車の周期の波長 を a(=2X+2Y) 、睡眠周期の波長を b(=P+Q) と置いた時に、
  # X <= ANS%m_1 < X+Y、P <= ANS%m_2 < P+Q となる最小の ANS を求める。
  # 高橋くんは過去にいけないので ANS >= 1
  # ここで ANS%m_1 = t、ANS%m_2 = s と置くと、ANS = m_1*p' + t = m_2*q' + s (p', q' は拡張ユークリッドの互除法 で求めることができる。)
  # s, t を決めた時、ANS を算出できる。
  # m_1*(p') - m_2+(q') =  s - t
  # 拡張ユークリッドの互除法 により、 a*p + b*q = d が求まるので、両辺に (s-t)/d を掛けて、
  # m_1*p*(s-t)/d + m_2*q*(s-t)/d = s - t
  # つまり、p' = p *(s-t)/d、q' = -q*(s-t)/d = q*(t-s)/d
  # 拡張ユークリッドの互除法、mod が互いに素じゃないと成り立たない・・・？
  # 中国剰余定理 (CRT) 解説 => https://qiita.com/drken/items/ae02240cd1f8edfc86fd
  # 互いに素でない場合 => https://qiita.com/drken/items/ae02240cd1f8edfc86fd#1-3-%E6%B3%95%E3%81%8C%E4%BA%92%E3%81%84%E3%81%AB%E7%B4%A0%E3%81%A7%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88%E3%81%B8%E3%81%AE%E6%8B%A1%E5%BC%B5

  for _ in range(T):
    X, Y, P, Q = map(int, input().split(" "))
    m_1 = 2*(X+Y)
    m_2 = P+Q
    d, p, q =extgcd(m_1, m_2)
    ans = inf
    for t in range(X, X+Y):
      for s in range(P, P+Q):
        x, r = crt(t, m_1, s, m_2, d, p, q)
        if x == -1: continue
        ans = min(ans, r)

    print(ans if ans != inf else "infinity")

resolve()

if __name__ == "__main__":
    unittest.main()
