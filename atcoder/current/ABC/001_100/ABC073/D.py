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

    def test_Sample_Input_1(self):
        input = """3 3 3
1 2 3
1 2 1
2 3 1
3 1 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 2
1 3
2 3 2
1 3 6
1 2 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 6 3
2 3 4
1 2 4
2 3 3
4 3 1
1 4 1
4 2 2
3 1 6"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  from heapq import heappop, heappush
  from itertools import permutations
  # 訪れる必要がある各街をスタートとして、ダイクストラする。
  # R <= 8 なので、順番は 8! = 40320 通りあって、これは十分小さいので全部試す。
  N, M, _ = map(int, input().split(" "))
  R = [int(x)-1 for x in input().split(" ")]

  PATH = [set() for _ in range(N)]
  for _ in range(M):
    A, B, C = [int(x)-1 for x in input().split(" ")]
    PATH[A].add((C+1, B))
    PATH[B].add((C+1, A))
  
  # R[i] を始点としたダイクストラをする。
  distance = [[inf]*N for _ in range(N)]
  for r in R:
    candidate = [(0, r)]
    dist_r = distance[r]

    while candidate:
      cost, i = heappop(candidate)
      if cost > dist_r[i]: continue
      dist_r[i] = cost

      for c, j in PATH[i]:
        if cost+c > dist_r[j]: continue
        heappush(candidate, (cost+c, j))
  
  ans = inf
  for per in permutations(R):
    temp = 0
    for i in range(len(per)-1):
      temp += distance[per[i]][per[i+1]]
    
    ans = min(ans, temp)


  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
