# 高速な組み合わせ計算
def comb(N, R, mod):
  if N-R < R: R = N-R

  # 分母を計算
  ans = 1
  for n in range(N-R+1, N+1):
    ans*=n
    if ans > mod: ans%=mod

  # 分子を計算
  den = 1
  for r in range(2, R+1):
    den*=r
    if den > mod: den%=mod

  ans *= pow(den, mod-2, mod)
  return ans%mod
