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

#     def test_Sample_Input_1(self):
#         input = """5 1
# 1 0 0 1 0"""
#         output = """1 2 2 1 2"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """5 2
# 1 0 0 1 0"""
#         output = """3 3 4 4 3"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """4 4
# 0 0 0 0"""
#         output = """4 4 4 4"""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 10
0 0 0 0 0 0 0 0 0 0"""
        output = """10 10 10 10 10 10 10 10 10 10"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 愚直にやっていくと間に合わなさそうなのでちょっと考える。
  # N も K も大きい。 <= 2*10**5
  # A' は N 以上にはならない。(場にある電球の数が N 個なので)
  # 明るさ 0 の電球は自身がいる座標を照らしている。(明るさ 0 != 明かりが出ていない)
  # K=5, [1 0 0 0 0] で考える。
  # [1 2 1 1 1] => [2 3 3 4 2] => [4 4 5 4 4] => [5 5 5 5 5] => [5 5 5 5 5]
  # K=4, [0 0 0 0]
  # [1 1 1 1] => [2 3 3 2] => [3 4 4 3] => [4 4 4 4]
  # 4 回目の操作の時点で収束する。
  # とりあえず早めに収束する前提で進めてみる。
  # => TLE した。意外と収束遅い？
  # => 10 10 で試してみたら打ち切り失敗してた。
  # 個数の計算は毎回 imos をするのが良さそう。
  # => imos を内包表記でやれたら間に合うかも
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  imos = [0]*(N)
  for _ in range(K):
    imos = [0]*N
    for i in range(N):
      imos[max(0, i-A[i])] += 1
      if i+A[i]+1 < N: imos[i+A[i]+1] -= 1

    fixed = int(A[0] == N)
    for i in range(1, N):
      A[i] = imos[i]+A[i-1]
      if A[i] == N: fixed+=1
    if fixed == N:
       break
  print(*A, sep=" ")

resolve()

if __name__ == "__main__":
    unittest.main()
