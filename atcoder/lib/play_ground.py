# from itertools import combinations, product, combinations_with_replacement
# import collections
# from math import gcd

# from math import sqrt
# inf = 10**18+1
# T = 1000
# C = 10
# D = 10000
# t = 30
# min_w = 0
# min_val = inf
# for w in range(T+1):
#   val = w+D//(t+w)
#   if min_val > val:
#     min_val = val
#     min_w = w
# print(min_val+t, w+t, sqrt(D))

def resolve():
  # N は 8 進数で最大 21 桁
  # N, K = input().split(" ")
  # K = int(K)
  N = "1152521504606546576"
  K = 100
  for _ in range(K):
    N = int(N, 8)
    nonary = ""
    while N != 0:
      s = str(N%9)
      nonary += s if s!="8" else "5"
      N//=9
    N = nonary[::-1]
  print(N)

resolve()