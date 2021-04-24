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
        input = """4 3
2 3 1 5
2 4
1 2
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
13 8 3 15 18
2 4
1 2
4 5
2 3
1 3"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 1
1 100 1
2 3"""
        output = """-99"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  inf = 10**10+1
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  # DP でやってみる
  roads = defaultdict(set)
  for _ in range(M):
    X, Y = [int(x)-1 for x in input().split(" ")]
    roads[X].add(Y)

  # j を i 番目の町から直接いける町だとすると、dp[j] = min(<i 番目の町まで見た時の最安値>, <j 番目の町まで見た時の最安値>, <i 番目の町での価格>)
  # 最初からトポロジカルソートされたような状態なので、dp の計算順序が前後することはない。
  # j 番目の町で売りたい時、j 番目の町で購入することはできないので、dp[j] の計算には j 番目の町の価格を入れることができない点に注意する。
  # X > Y 制約があるので、0 番目の町で売ることはない => 0 番目の町の最安値は知る必要がない。
  dp = [inf]*N
  for i in range(N):
    for next_ in roads[i]:
      dp[next_] = min(dp[i], dp[next_], A[i])

  ans = (-1)*inf
  for i in range(N):
    ans = max(ans, A[i] - dp[i])
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
