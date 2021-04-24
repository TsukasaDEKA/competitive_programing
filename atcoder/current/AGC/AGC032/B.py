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
        input = """3"""
        output = """2
1 3
2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  # 「ある整数 S が存在して、任意の頂点についてその頂点に隣接する頂点の番号の値の和は S となる」
  # とある。少なくとも一つの頂点は N の番号に連結しているので S >= N になるはずである。
  # S == N かつ番号 N 頂点に何かつなぐことを考えてみる。
  # 例えば、X + Y = S となる X, Y を繋いだ時、この時点で隣接する頂点の番号の和が S (N) になるので、それ以上接続することができない。
  # 例に出てくる N == 3 に頂点 4 を追加していくことを考える。1-2, 1-3, 2-4, 3-4 のように繋げば全ての頂点の隣接番号合計は 5 になる。
  # 例に出てくる N == 3 に頂点 4 を追加していくことを考える。1-2, 1-3, 2-4, 3-4 のように繋げば全ての頂点の隣接番号合計は 5 になる。
  # N が奇数の場合、合計が N になるペアを作る。(N はペア無し。)
  # N が偶数の場合、合計が N+1 になるペアを作る。
  # 自分のペア以外と接続するようにすれば全ての点において隣接マスの合計値が S = sum(1...N) - N (偶数の場合 N+1) になる。
  N = int(input())
  # 上手くいけば計算量減らせそうだけどめんどいので set でやる。N<=100 なので O(N**2)でも間に合う。
  ans = set()
  for n in range(1, N+1):
    for p in range(1, N+1):
      if n==p: continue
      if N%2 and p+n == N: continue
      if N%2==0 and p+n == N+1: continue
      ans.add((min(n, p), max(n, p)))
  print(len(ans))
  for a in sorted(list(ans)):
    print(*a)

resolve()

if __name__ == "__main__":
    unittest.main()
