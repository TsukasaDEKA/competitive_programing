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

#     def test_Sample_Input_1(self):
#         input = """2
# 35
# AT"""
#         output = """Takahashi"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """5
# 12345
# AAAAT"""
#         output = """Aoki"""
#         self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
67890
TTTTA"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
12345
ATATA"""
        output = """Aoki"""
        self.assertIO(input, output)

def resolve():
  # dp[i] = 
  # 
  N = int(input())
  S = [int(x) for x in list(input())]
  X = list(input())
  dp = [set() for _ in range(N+1)]

  dp[N].add(0)
  for i in reversed(range(1, N+1)):
    if X[i-1]=="A":
      for r in range(7):
        if r*10%7 in dp[i] and (r*10 + S[i-1])%7 in dp[i]:
          dp[i-1].add(r)
    else:
      for r in range(7):
        if r*10%7 in dp[i] or (r*10 + S[i-1])%7 in dp[i]:
          dp[i-1].add(r)

  print(dp)
  # print(T)
  print("Takahashi" if (0 in dp[0]) else "Aoki")

# resolve()

if __name__ == "__main__":
    unittest.main()