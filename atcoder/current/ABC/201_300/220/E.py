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
        input = """3 2"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """14142 17320"""
        output = """11284501"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ
 
  mod = 998244353
  inf = 10**18+1
  # 深さは 0 ~ N-1 まで
  # 深さを d とすると深さ d の頂点は 2**(d) 個ある。
  # その頂点を通ってかつそれより根の方向に進まない経路を考える。
  # 根を通る長さが D の経路について考える。
  # 左側から i 、右側から j を取ってくる時に、i の深さを d_i とすると、j 側の深さは D-d_i となる。
  # i 側の取り方は 2**(max(0, d_i-1)) パターンで j の取り方は 2**(max(0, D-d_i-1)) パターン
  # なので、根を通る経路で長さが D のものの個数は 2**(max(0, d_i-1) + max(0, D-d_i-1)) になる。
  # 累積和を取ればいい感じにできそう。
  N, D = map(int, input().split(" "))

  table = [pow(2, max(0, i-1) + max(0, D-i-1), mod) for i in range(N)]
  # 累積和をとる。
  table = [0] + list(accumulate(table))
 
  ans = 0
  for i in range(N):
    if 2*(N-1-i) < D: break
    max_d = min(D, N-1-i)
    min_d = max(0, D-(N-1-i))
    ans += (table[max_d+1]-table[min_d])*pow(2, i, mod)
    if ans >= mod: ans%=mod

  print((ans*2)%mod)
 
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
