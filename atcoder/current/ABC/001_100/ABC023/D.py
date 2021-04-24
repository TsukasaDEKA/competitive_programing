import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff=None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """4
5 6
12 4
14 7
21 2"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
100 1
100 1
100 1
100 1
100 1
1 30"""
        output = """105"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 最終得点はできるだけペナルティを平均化するのが良さそう。
  # N <= 10**5 なので O(N**2) だと厳しい
  # i 番目に割る風船のペナルティは H+S*i になる。
  # 最終得点が max(H) を下回ることがない。
  # 入力例 1 は H が高い順に割っても成り立つ。
  # i の範囲は 0 ~ N なので、[H+S*i for i, H, S in enumrate(H_S)] みたいにすれば風船 Bn を割った時にとりうる値が全てわかる。
  # Bn のとりうる値を全部探索していくとか？
  # 必ずどれかの風船が最後に撃たれるので、min([H+S*(N-1) for H, S in H_S]) が答え？
  # min(Hi+S*N) < max(Hi) の場合があるため、そうはならない。
  # ただ、少なくとも答えは min([H+S*(N-1) for H, S in H_S]) 以上になる。
  # なので、min([H+S*(N-1) for H, S in H_S]) は取った方が良さげ。
  # dp[N][N] 確保するとメモリが足りない。
  # min(Hi+S*N) => max(Hi) の間に 答えはある？
  # もしかして 1 次元 DP でいける？

  # H <= 10**9、S <= 10**9、N <= 10**5なので、最高到達高度は H+S*N で 10**9 + 10**(9+5) 程度。
  # なので、log(H+S*N) < 80 くらい
  # O(N*log(H+S*N)) くらいの計算量だったら間に合う
  # min(Hi+Si*N) ~ max(Hi+Si*N) で二分探索をしていって、まず答えを決めて、その答えが達成できるかを O(N) で判定する。
  # min、max を出す必要はないかも 0 ~ 10**9 + 10**(9+5) でも十分間に合いそう。
  # 答えを X と仮置きした時に、その答えが達成できる場合、全ての風船の高度が X を超える前に撃てば良い。
  # 風船 Bi を T 秒以内に撃てば高度 X を超えない、というのを式で表すと Ti = (X - Hi)//Si
  # C[t]: t 秒までに撃たなきゃいけない風船の個数 とすると、任意の j において sum(C[:j]) <= j となれば良い。
  # 例: 1 秒以内に撃ち落とさなきゃいけない風船が 5 個ある場合、sum(C[:5]) = 5 > j で達成不可
  # 例: 1 秒以内に撃ち落とさなきゃいけない風船が 1 個、2秒以内が 1 個の場合、sum(C[:1]) = 1 <= 1、sum(C[:2]) = 2 <= 2 で達成可

  N = int(input())
  H_S = [list(map(int, input().split(" "))) for _ in range(N)]

  from collections import Counter
  # 二分探索
  def solve(x):
    # 高度 x に到達するまでに全部撃てるか判定
    C = Counter([min(N-1, max(-1, x-h)//s) for h, s in H_S])
    # -1 が含まれる => x < Hi の組み合わせが存在する場合は達成不可
    if -1 in C: return False
    count = 0
    for n in range(N):
      if n in C:
        count += C[n]
        if count > n+1:
          return False
    return True

  # メグル式二分探索。
  def binary_search(ng, ok, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid
    
    # 探索範囲内で見つからなかった場合、-1 を返す 
    # これだと index out of range になる場合があるので注意
    return ok

  ng = 0
  ok = 10**9+10**(9+5)+1

  print(binary_search(ng, ok, solve))

resolve()

if __name__ == "__main__":
    unittest.main()
