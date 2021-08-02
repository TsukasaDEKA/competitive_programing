# 高速組み合わせ計算
# 高速組合せ計算
# nCr
# comb
# mod

# 0 <= r <= N の範囲で nCr のリストを返す。
# 逆元を使っているので mod が素数かつ n より大きくないと変な動きするかも
def nCr_list(N, mod):
  comb = [1]*(N+1)
  comb[1] = comb[N-1] = N
  for r in range(2, N//2+1):
    diff = (N-r+1)*pow(r, mod-2, mod)%mod
    comb[r] = comb[N-r] = (comb[r-1]*diff)%mod
  return comb

mod = 998244353
# sample 
_ = nCr_list(10**7, mod)