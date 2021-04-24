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
        input = """3 8
3 3
4 5
5 6"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1000000000
1000000000 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10
  N, W = map(int, input().split(" "))

  items = []
  for _ in range(N):
    items.append([int(x) for x in input().split(" ")])
  items.sort()

  V = 0
  for item in items:
    V += item[1]
 
  dp = [inf]*(V+1) for _ in range(N+1)
  dp[0] = 0

  for n in range(1, N+1):
    weight, value = items[n-1]
    for v in range(V+1):
      if v-value >= 0:
        recent_val = dp[n-1][v-value] + weight
        if recent_val > W: recent_val = inf
        dp[n][v] = min(recent_val, dp[n-1][v])
      else:
        dp[n][v] = dp[n-1][v]
  # print()
  # for DP in dp:
  #   print(DP)
  # print()

  ans_index = V
  while dp[-1][ans_index] > W:
    ans_index -= 1
    if ans_index == 0: break
  print(ans_index)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
