# メグル式二分探索。
def binary_search(ng, ok, solve):
  while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if solve(mid): ok = mid
    else: ng = mid

  # 探索範囲内で見つからなかった場合、-1 を返す 
  return ok if solve(ok) else -1

def sample():
  def solve(x):
    return A[x] <= 10

  for i in range(15):
    A = list(range(i, i+5))
    ng = len(A)
    ok = 0
    # print(i, A)
    print(A[binary_search(ng, ok, solve)])

sample()