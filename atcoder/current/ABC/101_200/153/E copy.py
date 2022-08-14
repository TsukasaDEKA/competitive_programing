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
        input = """9 3
8 3
4 2
2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100 6
1 1
2 3
3 9
4 27
5 81
6 243"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9999 10
540 7550
691 9680
700 9790
510 7150
415 5818
551 7712
587 8227
619 8671
588 8228
176 2461"""
        output = """139815"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 個数制限無し DP 
  # DP サイズは 10**7 なので足りそう。
  H, N = map(int, input().split(" "))
  spells = [None]*N
  max_attack = 0
  for i in range(N):
    spells[i] = [int(x) for x in input().split(" ")]
    max_attack = max(max_attack, spells[i][0])

  dp = [inf]*(H+max_attack+1)
  dp[0] = 0
  ans = inf
  # dp[i] = ダメージの総和が i になるように選んだ時の魔力の最小値
  for i in range(H):
    for j in range(N):
      dp[i+spells[j][0]] = min(dp[i+spells[j][0]], dp[i]+spells[j][1])
      if i+spells[j][0] >= H: ans = min(ans, dp[i+spells[j][0]])
  print(ans)
  # print(*dp, sep="\n")
resolve()

if __name__ == "__main__":
    unittest.main()
