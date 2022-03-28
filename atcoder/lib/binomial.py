# 二項係数
# nCr
# comb, cmb, comb_mod

# 0 ~ N までの二項係数テーブルを作る。
# O(N**2) の計算量、メモリ空間がかかる点に注意する。
# N <= K*10**3 程度ならいける。
class Binomial:
  def __init__(self, n, mod):
    self.binomial = [[0]*(n+1) for _ in range(n+1)]
  
    for i in range(n+1):
      for j in range(i+1):
        if j > i: break
        if i == 0 or j == 0:
          self.binomial[i][j] = 1
          continue
        self.binomial[i][j] = (self.binomial[i-1][j-1] + self.binomial[i-1][j]) % mod

  def get(self, n, r):
    return self.binomial[n][r]