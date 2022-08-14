import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
# product('ABCD', repeat=2) => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
from itertools import product
# permutations('ABCD', 2) => AB AC AD BA BC BD CA CB CD DA DB DC
from itertools import permutations
# combinations('ABCD', 2) => AB AC AD BC BD CD
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left
# 0埋めされた二進数表現
f'{9:05b}'

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]
dh8 = [-1, -1, -1,  0,  0,  1,  1,  1]
dw8 = [-1,  0,  1, -1,  1, -1,  0,  1]

def resolve():
  mod = 998244353
  N, M, K = map(int, input().split(" "))
  DEGREES = [0]*N
  for _ in range(M):
    u, v = [int(x)-1 for x in input().split(" ")]
    DEGREES[u] += 1
    DEGREES[v] += 1

  # 次数が奇数の頂点の個数を求める。
  odd_deg_count = 0
  for i in range(N):
    if DEGREES[i]%2: odd_deg_count += 1
  even_deg_count = N-odd_deg_count

  # 毎回組み合わせ数を計算してると時間がかかるので、あらかじめテーブルを作っておく。
  # odd_comb_table[n] := 次数が奇数の頂点から n 個選ぶ時の塗り方の個数
  odd_comb_table = [1, odd_deg_count]
  for i in range(2, odd_deg_count+1):
    val = odd_comb_table[-1]
    val = (val*(odd_deg_count-i+1))%mod

    # 逆元をかける
    val = val*pow(i, mod-2, mod)%mod
    odd_comb_table.append(val)

  # even_comb_table[n] := 次数が偶数の頂点から n 個選ぶ時の塗り方の個数
  even_comb_table = [1, even_deg_count]
  for i in range(2, even_deg_count+1):
    val = even_comb_table[-1]
    val = (val*(even_deg_count-i+1))%mod

    # 逆元をかける
    val = val*pow(i, mod-2, mod)%mod
    even_comb_table.append(val)

  # 次数が奇数の頂点を偶数個塗る塗り方がいくつあるか数える。
  ans = 0
  for n in range(0, min(odd_deg_count, K)+1, 2):
    # 次数が奇数の頂点を n 個塗ったあと、残り K-n 個塗らなきゃいけない。
    # その個数が次数が偶数の頂点の個数を超えていたら条件を満たす塗り方は存在しない。
    if K-n > even_deg_count: continue
    temp = 1
    # 次数が奇数の頂点を偶数個塗る
    temp *= odd_comb_table[n]
    if temp >= mod: temp%=mod

    # 次数が偶数の頂点を塗って、赤く塗られた頂点が K 個になるようにする。
    temp *= even_comb_table[K-n]
    if temp >= mod: temp%=mod

    ans += temp
    if ans >= mod: ans%=mod
  print(ans)

resolve()