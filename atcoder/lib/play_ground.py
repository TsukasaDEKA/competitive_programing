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


for n in range(1, 10):
  N = 1<<(n)
  val = [0]*(n)
  count = 0
  for i in range(N):
    if "11" in bin(i): continue
    count+=1
    for j in range(n):
      if (i>>j)&1:
        val[j]+=1
  ans = [count-2*v for v in val]
  ans_2 = [ans[i]-ans[i+1] for i in range(n-1)]
  print(n, count, val)
  # print(n, count, ans)
  # print(sum(val), val)
