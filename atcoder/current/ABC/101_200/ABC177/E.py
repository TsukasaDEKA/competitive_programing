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
3 4 5"""
        output = """pairwise coprime"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
6 10 15"""
        output = """setwise coprime"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
6 10 16"""
        output = """not coprime"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3
1 1 1"""
        output = """pairwise coprime"""
        self.assertIO(input, output)

def resolve():
  A_max = 10**7
  # 制約がキツめ。O(N) とか O(N*logN) くらいで解きたい。
  # 最大公約数を求める必要はなくて、同じ素因数が含まれているかチェックすれば良い。
  # 全部の約数を列挙して、集計して、それぞれの約数の個数をカウントする。
  # 約数の個数が全て 1 => pairwise coprime
  # 約数の個数の中に 1 以外が含まれ、かつそれが N 個でない => setwise coprime
  # 約数の個数の中に N 個のものが含まれる => not coprime
  # 約数列挙に sqrt(N) 程度の計算をしなきゃいけないのでちょっと辛い。
  # 素因数分解をメモ化してやればいける？
  # 高速素因数分解で調べた結果 => https://qiita.com/ganariya/items/fba261ee53a5b6decc47
  # 上記のやり方を試してみる。

  N = int(input())
  A = [int(x) for x in input().split(" ")]

  # min_prime_factor[i] : i に含まれる最小の素数
  min_prime_factor = list(range(A_max+1))
  min_prime_factor[0] = min_prime_factor[1] = 1
  for i in range(2, int(-(-A_max**0.5//1))+1):
    if min_prime_factor[i] == i:
      for j in range(i*i, A_max+1, i):
        if min_prime_factor[j] == j: min_prime_factor[j] = i
  
  from collections import defaultdict

  primes_count = defaultdict(int)
  # 1 要素あたり最大 60 回程度の処理しかやらないはず。
  for a in A:
    if a == 1: continue
    temp_primes = set()
    while a > 1:
      temp_primes.add(min_prime_factor[a])
      a//=min_prime_factor[a]
    for prime in temp_primes: primes_count[prime] += 1

  counts = set(primes_count.values())
  if len(counts) == 0:
    print("pairwise coprime")
    return

  if len(counts) == 1 and list(counts)[0] == 1:
    print("pairwise coprime")
    return

  if N not in counts:
    print("setwise coprime")
    return

  print("not coprime")

resolve()

if __name__ == "__main__":
    unittest.main()
