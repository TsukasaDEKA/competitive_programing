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
5 2 7 6
1 1 3 1
999999999 1 1000000000 1"""
        output = """20
infinity
1000000000999999999"""
        self.assertIO(input, output)

def resolve():
  def extgcd(a, b):
    # ax + by = d (d = 最大公約数) とした時、d, x, y を返す。
    if b:
      g, y, x = extgcd(b, a % b)
      y -= (a // b)*x
      return g, x, y
    return a, 1, 0

  # 参考: https://qiita.com/drken/items/ae02240cd1f8edfc86fd
  def crt(b1, m1, b2, m2, d=None, p=None, q=None):
    # x ≡ b1 (mod m1)、x ≡ b2 (mod m2) <=> x ≡ r (mod lcm(m1, m2)) となる x, r を返す。
    # また、解が存在しない時、それを示す。
    if d is None: d, p, q = extgcd(m1, m2)
    # 解が存在しない場合 => m1, m2 が互いに素ではなく、かつ b1 ≡ b2 (mod. gcd(m1, m2)) が成立しない。
    if d != 1 and b1%d != b2%d: return -1, -1

    x = b1 + m1*p*(b2-b1)//d
    r = x%((m1*m2)//d)
    return x, r

  inf = 10**30
  # 電車の移動周期は 2(X+Y) => 街 B には (2X+2Y)*N + X ~ (2X+2Y)*N + X+Y の間に停車している。
  # 高橋くんの睡眠周期は P, Q
  T = int(input())
  for _ in range(T):
    X, Y, P, Q = map(int, input().split(" "))
    m_1, m_2 = 2*(X+Y), P+Q
    ans = inf
    for y in range(X, X+Y):
      for q in range(P, P+Q):
        x, r = crt(y, m_1, q, m_2)
        if x == -1: continue
        ans = min(ans, r)

    print(ans if ans != inf else "infinity")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()