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
        input = """axyb
abyxb"""
        output = """ayb"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """aa
xayaz"""
        output = """aa"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """a
z"""
        output = """"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """abracadabra
avadakedavra"""
        output = """aaadara"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """aaaaaaaal
bbbbbbbbbb"""
        output = """"""
        self.assertIO(input, output)

import copy
def resolve():
  S = [" "]
  S.extend(list(input()))
  T = [" "]
  T.extend(list(input()))

  if len(S) > len(T):
    tempS = copy.deepcopy(S)
    S = copy.deepcopy(T)
    T = tempS

  dp = [[0]*(len(T)) for _ in range(len(S))]
  for s_i in range(1,len(S)):
    for t_i in range(1,len(T)):
      if S[s_i] == T[t_i]:
        dp[s_i][t_i] = dp[s_i - 1][t_i - 1] + 1
      else:
        dp[s_i][t_i] = max(dp[s_i][t_i - 1], dp[s_i - 1][t_i])
  # print()
  # for d in dp:
  #   print(d)
  # print(" ", end="")
  # for t in T:
  #   print(t+", ", end="")
  # print(" ")
  # print(" ", end="")
  # for i in range(len(T)):
  #   print(str(i)+", ", end="")

  ans = ""
  t_search_start_i = len(T)
  current = dp[-1][-1]
  for s_i in reversed(range(1,len(S))):
    for t_i in reversed(range(1, t_search_start_i)):
      if dp[s_i][t_i] != current: break
      if dp[s_i-1][t_i-1] == current - 1 and dp[s_i][t_i-1] != current and dp[s_i-1][t_i] != current and S[s_i] == T[t_i]:
        current = dp[s_i-1][t_i-1]
        # print(str(t_i) + ",", end="")
        ans = T[t_i] + ans
        t_search_start_i = t_i
        break
  print(ans)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
