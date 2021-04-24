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
        input = """3 3
1 2
1 3 3
3 2 3
1 2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 4
1 3
1 2 2
1 4 3
2 4 3
3 4 5"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush
  inf = 10**18+1
  # ワーシャルフロイド応用？街の数が 1000 あるので間に合わないかも。
  # ダイクストラでいけそう。
  # s からの最短経路と、t からの最短経路を求めて、それが一致する街を探す。
  # 最強最速なのに、t -> u の過程で s を通るのは有り？ -> そんなことは有りえないのでセーフ
  # 速度的には問題なさそうだけど WA するのなんで？
  N, M = map(int, input().split(" "))
  S, T = [int(x)-1 for x in input().split(" ")]
  ROUTS = [list(map(int, input().split(" "))) for _ in range(M)]
  route = [set() for _ in range(N)]
  for x, y, d in ROUTS:
    x-=1
    y-=1
    route[x].add((d, y))
    route[y].add((d, x))

  candidate = [(0, S)]
  d_from_s = [inf]*N

  while candidate:
    cost, i = heappop(candidate)
    if cost > d_from_s[i]: continue
    d_from_s[i] = cost

    for c, j in route[i]:
      if cost + c > d_from_s[j]: continue
      heappush(candidate, (cost+c, j))

  candidate = [(0, T)]
  d_from_t = [inf]*N

  while candidate:
    cost, i = heappop(candidate)
    if cost > d_from_t[i]: continue
    d_from_t[i] = cost

    for c, j in route[i]:
      if cost + c > d_from_t[j]: continue
      heappush(candidate, (cost+c, j))

  for i in range(N):
    if d_from_s[i] == d_from_t[i] and d_from_s[i] != inf:
      print(i+1)
      return

  # print(d_from_s, d_from_t)
  print(-1)

# resolve()

if __name__ == "__main__":
    unittest.main()
