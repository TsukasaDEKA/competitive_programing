
from random import randint
N = 1500
k = randint(0, N)
# k = N-1
judge = [0]*N
judge[0] = N*10+randint(1, 10)
for i in range(1, N):
  judge[i] = judge[i-1]
  if i <= k: judge[i]+=randint(1, 10)
  else: judge[i]-=randint(1, 10)

import sys
def update(x, memo):
  if memo[x] < 0:
    if sys.argv[-1] == './Main.py':
      print("?", x+1, sep=" ")
      memo[x] = int(input())
    else:
      memo[x] = judge[x]

def resolve(N):
  # 見る区間が l, r だとして、中心座標 c を決める。
  # A[(c+l)//2] < A[c] < A[(c+r)//2] の場合、 [c, r] の間に答えがある。=> l = c にする。
  # A[(c+l)//2] < A[c] > A[(c+r)//2] の場合、[(c+l)//2, (c+r)//2] の間に答えがある。 => l = (c+l)//2, r = (c+r)//2 にする。
  # A[(c+l)//2] == A[c] だった場合、[(c+l)//2, c] の間に答えがある。
  # A[c] == A[(c+r)//2] だった場合、[c, (c+r)//2] の間に答えがある。
  # 半開区間で見た方が楽そう。
  max_query = 15
  count = 0
  loop_limit = 200
  loop_count = 0
  ans = [-1]*N

  if N <= 15:
    for i in range(N):
      update(i, ans)
    return max(ans)
  L = 0
  R = N
  c = (L+R)//2
  while abs(L-R) > 1 and count < max_query and loop_count < loop_limit:
    loop_count+=1
    # print(ans)
    # 見る範囲が残りのクエリ数よりも少ない場合、全部確認する。
    if ans[L:R].count(-1) <= max_query-count:
      for i in range(L, R): update(i, ans)
      break

    if ans[c] < 0: count+=1
    update(c, ans)

    l = (c+L)//2
    r = (c+R)//2
    if ans[l] < 0: count+=1
    update(l, ans)
    if ans[l] >= ans[c]+abs(l-c):
      R = c
      c = l
      continue

    if ans[l] >= ans[c]-abs(l-c):
      L = l
      R = c
      c = (L+R)//2
      continue

    if ans[r] < 0: count+=1
    update(r, ans)
    if ans[c]+abs(r-c) <= ans[r]:
      L = c
      c = r
      continue
    if ans[c]-abs(r-c) <= ans[r]:
      L = c
      R = r
      c = (L+R)//2
      continue

    L = l+1
    R = r

  # print(L, R)
  # print(count)
  # print(ans)
  return max(ans)
  # print("!", max(ans), sep=" ")

if sys.argv[-1] == './Main.py':
  T = int(input())
  for _ in range(T):
    print("!", resolve(int(input())), sep=" ")
else:
  ans = resolve(N)
  print(ans, ans == max(judge))
