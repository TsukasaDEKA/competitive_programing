import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """4 5
2 5 7 3
1 2 1
1 3 2
2 4 4
3 4 3
2 3 2"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 5
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
1 2 1000000000
2 3 1000000000
3 4 1000000000
4 5 1000000000
5 6 1000000000"""
        output = """6000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  from heapq import heappop, heappush
  # 遷移の時に満足度を配れば良さそう。
  # ダイクストラして、更新が走ったタイミングで満足度も更新する。
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  ROUTE = [set() for _ in range(N)]
  for i in range(M):
    U, V, T = [int(x) for x in input().split(" ")]
    ROUTE[U-1].add((T, V-1))

  ans = [0]*N
  candidate = [(0, 0, 0)]
  distance = [inf]*(N)

  while candidate:
    cost, i, f = heappop(candidate)
    if cost > distance[i]: continue
    # distance[i] > cost の場合、強制書き換え。distance[i] == cost の場合、大きい方をとる。
    if distance[i] == cost:
      ans[i] = max(ans[i], A[i]+ans[f])
    else:
      ans[i] = A[i]+ans[f]
    distance[i] = cost

    for c, j in ROUTE[i]:
      if cost + c > distance[j]: continue
      heappush(candidate, (cost + c, j, i))

  # print(ans)
  print(ans[-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()