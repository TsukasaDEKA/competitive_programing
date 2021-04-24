# from itertools import combinations, product, combinations_with_replacement
# import collections
# from math import gcd

# from math import isqrt
# def factorization(n):
#   arr = []
#   temp = n
#   for i in range(2, int(-(-n**0.5//1))+1):
#     if temp%i==0:
#       cnt=0
#       while temp%i==0:
#         cnt+=1
#         temp //= i
#       arr.append([i, cnt])

#   if temp!=1:
#     arr.append([temp, 1])

#   if arr==[]:
#     arr.append([n, 1])

#   return arr

# print(factorization(998244353))

# from itertools import accumulate
# sample = list(range(10))
# print(sample[:len(sample)])

# mod = 10**9+7
# def comb_mod(n,r,mod):
#   if n-r<r:
#     r=n-r
#   N=n
#   R=r
#   u=1
#   d=1
#   for i in range(r):
#     u*=N
#     u%=mod F
#     N-=1
#     d*=R
#     d%=mod
#     R-=1
#   return u*pow(d,mod-2,mod)%mod

# from time import time

# N = 10**4
# start = time()
# for i in range(N):
#   comb_mod(i, i//2, mod)
#   # print()

# print(time()-start)
# for i in permutations(sample):
#   print(i)
# print(["_"]*3)


sample = """127
33
18
13
10
8
7"""

sample = [int(x) for x in sample.split("\n")]
# print(sample[0])
