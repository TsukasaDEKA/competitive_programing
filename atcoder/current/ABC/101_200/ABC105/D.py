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
        input = """3 2
4 1 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """13 17
29 7 5 7 9 51 7 13 8 55 42 9 81"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 400000000
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """25"""
        self.assertIO(input, output)

def resolve():
  # 各 Ai は M の余りをとっておく。
  # => Ai = ki*M + Ai%M と表現した時、区間 l-r の和が M の倍数かどうかは
  # => Al%M ~ Ar%M の和が M の倍数かどうかに依存し、kl*M ~ kr*M の和に依存しないので除外して考えることができるため。
  # A の累積和 (sumA とする) を取った時、sumA[i]%M が一致する l, r の組みを考えると、
  # sumA[r]-sumA[l] は M の倍数になる。
  # 上記のことから、M で割った余りが一致する sumA[i] の個数を数えて、その中から 2 個選ぶ組み合わせ数を求めれば良い。
  # 組み合わせ数は nC2 で求めることができる。
  from collections import defaultdict
  N, M = map(int, input().split(" "))
  A = [int(x)%M for x in input().split(" ")]
  # 累積和をとる。
  sumA = [0]*(N+1)
  for i in range(N):
    sumA[i+1] = A[i]+sumA[i]

  # M で割った余りが一致するものを集計する。
  agg = defaultdict(int)
  for i in range(N+1):
    agg[sumA[i]%M]+=1

  # 組み合わせ数を計算
  ans = 0
  for v in agg.values():
    ans+= (v*(v-1))//2
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()