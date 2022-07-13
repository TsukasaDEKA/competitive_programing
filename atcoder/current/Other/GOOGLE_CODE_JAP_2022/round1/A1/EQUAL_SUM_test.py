import sys
def resolve():
  from collections import defaultdict
  T = int(input())

  for t in range(1, T+1):
    N = int(input())
    used = set()
    request = []
    for i in range(N):
      val = pow(2, i)
      if val >= 10**9: break
      used.add(val)
      request.append(val)

    j = 2
    for _ in range(N - len(request)):
      while j in used:
        j+=1
      request.append(j)
      j += 1

    print(*request)
    response = [int(x) for x in input().split(" ")]

    A = sorted(request+response, reverse=True)

    goal = sum(A)//2
    ans = []
    for i in range(2*N):
      if A[i] <= goal:
        ans.append(A[i])
        goal -= A[i]
    # print(*A, file=sys.stderr)
    # print(goal, file=sys.stderr)
    # print(ans, file=sys.stderr)
    print(*ans, sep=" ")


resolve()
