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
  from heapq import heappop, heappush
  inf = 10**6+1

  N, M = map(int, input().split(" "))
  route = [set() for _ in range(N)]
  for _ in range(M):
    a, b, t = [int(x)-1 for x in input().split(" ")]
    t += 1
    route[a].add((t, b))
    route[b].add((t, a))

  ans = inf
  for start in range(N-1):
    candidate = [(0, start)]
    distance = [inf]*N
    # tar_count = 0
    while candidate:
      cost, i = heappop(candidate)
      if cost > distance[i]: continue
      distance[i] = cost
      # tar_count += 1

      for c, j in route[i]:
        if cost + c > distance[j]: continue
        distance[j] = cost + c
        heappush(candidate, (cost+c, j))
    ans = min(ans, max(distance))
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
