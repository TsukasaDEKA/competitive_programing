# https://qiita.com/ganariya/items/fba261ee53a5b6decc47
# エラトステネスの篩 (ふるい)
# prime[i] : i が素数かどうかの boolean
def get_primes(n):
  prime = ([False, True] * (n//2+1))[0: n+1]
  prime[1] = False
  prime[2] = True
  for i in range(3, int(-(-n**0.5//1))+1, 2):
    if not prime[i]: continue
    for t in range(i*i, n+1, i): prime[t] = False
  return prime

sample = 10**6
# get_primes(sample)
print([i for i, is_prime in enumerate(get_primes(sample)) if is_prime])

