# それぞれの A[i] を先頭にした最長増加部分列 (lis) の長さの配列を返す。
# # A = [1, 2, 4, 3, 2] の時、result = [1, 2, 3, 3, 2]
# 広義単調増加の場合は bisect_right を使う。

from bisect import bisect_left
def lis(x):
  inf = 10**18+1
  N = len(x)
  result = [0]*N
  LIS = [inf]*N
  for i in range(N):
    j = bisect_left(LIS, x[i])
    LIS[j] = x[i]
    result[i] = j+1
  return result
