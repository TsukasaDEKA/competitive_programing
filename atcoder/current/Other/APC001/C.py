N=99999
test_case = []
for i in range(N//2):
  test_case.extend([1,2])
test_case.append(1)
print(len(test_case))
state_str = ["Vacant", "Male", "Female"]

is_dev = True
# is_dev = False

def query(i):
  if is_dev:
    print(i, state_str[test_case[i]])
    return state_str[test_case[i]]
  print(i)
  return input()

def solve(mid, first_seat):
  result = query(mid)
  if result == "Vacant":
    exit(0)
  if mid%2:
    return result!=first_seat
  return result==first_seat

def resolve():
  # N <= 99999 でクエリが 20 までなので O(logN) 解がありそう。
  # i = 0 と i = N//2 を確認して、
  # 同性だったら N//2 ~ N までの間に少なくとも 1 つ空席があるので、i = N//2+N//4 を確認。
  # 異性だったら 0 ~ N//2 までの間に少なくとも 1 つ空席があるので、i = N//2-N//4 を確認。
  # 同じように、i = 0 と同性か異性かで次に確認する席を N//(2**クエリ回数) 分足し引きして決めていく。
  # 1/2 づつ探索範囲は狭まっていくので、N=99999 でも2**17 程度 (最後 + 1 回があるかも) で全て探索しきるはず。 
  # N = 
  N = len(test_case) if is_dev else int(input()) 
  # 0 番目のシートから確認開始。
  first_seat = query(0)
  if first_seat == "Vacant":
    return
  
  ok = 0
  ng = N
  count = 2
  while abs(ok-ng) > 1 and count <= 20:
    mid = (ok+ng)//2
    count+=1

    if solve(mid, first_seat):
      ok = mid
    else:
      ng = mid

resolve()
