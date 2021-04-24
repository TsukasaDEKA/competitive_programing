# 高速素因数分解 => https://qiita.com/ganariya/items/fba261ee53a5b6decc47
# prime_factors[i] : i に含まれる最小の素数
def get_min_prime_factor(n):
  prime_factors = list(range(n+1))
  prime_factors[0] = prime_factors[1] = 1
  for i in range(2, int(-(-n**0.5//1))+1):
    if prime_factors[i] == i:
      for j in range(i*i, n+1, i):
        if prime_factors[j] == j: prime_factors[j] = i
  return prime_factors

get_min_prime_factor(10**7)