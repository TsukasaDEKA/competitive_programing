import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """3 2
1 2 10
2 3 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 5
1 2 12
2 3 14
3 4 7
4 5 9
5 1 18"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 6
1 2 1
2 3 1
3 4 1
4 1 1
1 3 1
4 2 1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # N <= 300 で 300*300 だとまぁ間に合う。
  # M <= 44850 の 44850 ってなんだろ。=> 1 ~ 299 の和
  # 素朴に全探索すると 300*300 で間に合いそう
  from heapq import heapify, heappop, heappush
  from collections import defaultdict
  inf = 10**12+1

  N, M = map(int, input().split(" "))
  route = [set() for _ in range(N)]
  costs = [[inf]*N for _ in range(N)]
  for _ in range(M):
    a, b, t = [int(x)-1 for x in input().split(" ")]
    t += 1
    costs[a][b] = costs[b][a] = t
    route[a].add(b)
    route[b].add(a)

  # worst = [0]*N
  ans = inf
  max_heap = 0
  for start in range(N-1):
    candidate = []
    heapify(candidate)
    distance = [inf]*N
    distance[start] = 0
    fixed = [False]*N
    fixed[start] = True
    tar = set(list(range(start+1, N)))
    for i in route[start]:
      distance[i] = costs[start][i]
      heappush(candidate, [costs[start][i], i])

    temp_d = worst[start]
    while candidate and tar:
      max_heap = max(max_heap, len(candidate))
      cost, i = heappop(candidate)
      if fixed[i]: continue
      fixed[i] = True

      if i in tar: tar.remove(i)

      temp_d = max(temp_d, cost)
      worst[i] = max(worst[i], cost)

      for j in route[i]:
        if fixed[j]: continue
        heappush(candidate, [cost+costs[i][j], j])
    # print(start, temp_d)
    ans = min(ans, temp_d)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
