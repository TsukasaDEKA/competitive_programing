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

#     def test_Sample_Input_1(self):
#         input = """2
# 0 0 0
# 1 2 3"""
#         output = """9"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
0 0 0
1 1 1
-1 -1 -1"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """17
14142 13562 373095
-17320 508075 68877
223606 -79774 9979
-24494 -89742 783178
26457 513110 -64591
-282842 7124 -74619
31622 -77660 -168379
-33166 -24790 -3554
346410 16151 37755
-36055 51275 463989
37416 -573867 73941
-3872 -983346 207417
412310 56256 -17661
-42426 40687 -119285
43588 -989435 -40674
-447213 -59549 -99579
45825 7569 45584"""
        output = """6519344"""
        self.assertIO(input, output)

def cost(cityA, cityB):
  return abs(cityA[0] - cityB[0]) + abs(cityA[1] - cityB[1]) + max(0, cityB[2] - cityA[2])


def resolve():
  N = int(input())
  city_pos = [[int(x)for x in input().split(" ")] for _ in range(N)]

  inf = 10**10
  N2 = 1<<N
  dp = [[inf]*N for _ in range(N2)]

  # 都市間移動コスト
  costs = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      costs[i][j] = cost(city_pos[i], city_pos[j])
  # dp 計算
  ## dp 初期値 (0 から最初の都市に移動するコスト)
  for i in range(N):
    dp[1<<i][i] = costs[0][i]

  for i in range(N2):
    # print(dp)
    for j in range(N):
      # 頂点集合 (i) の中に移動元の頂点が含まれていなかったらスキップ
      if not i>>j&1: continue
      for k in range(N):
        # 移動先が頂点集合 (i) に含まれてたらスキップ
        if i>>k&1: continue
        dp[i|1<<k][k] = min(dp[i|1<<k][k], dp[i][j]+costs[j][k])

  # print(dp)

  print(dp[N2-1][0])

resolve()

if __name__ == "__main__":
    unittest.main()
