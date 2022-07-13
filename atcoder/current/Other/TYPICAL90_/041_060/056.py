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

    def test_入力例_1(self):
        input = """3 34
3 14
15 9
26 5"""
        output = """BAB"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 77
1 16
3 91
43 9
4 26
23 11"""
        output = """BABBA"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 59
8 13
55 5
58 8
23 14
4 61"""
        output = """Impossible"""
        self.assertIO(input, output)

def resolve():
  # N <= 100 なので Bit DP だと TLE
  # まず DP で解く。
  # dp[i][j] : i 番目までの商品を取った時、j 円である組み合わせが存在する
  # dp[N-1][S] が True である場合、末尾から復元していく。
  # O(N*S)
  N, S = map(int, input().split(" "))
  A_B = [[int(x) for x in input().split(" ")] for _ in range(N)]
  dp = [[0]*(S+1) for _ in range(N+1)]
  dp[0][0] = 1
 
  A, B = A_B[0]
  if A <= S: dp[1][A] = 1
  if B <= S: dp[1][B] = 1
 
  # 構築パート
  for i in range(1, N):
    A, B = A_B[i]
    for j in range(min(A, B), S+1):
      if dp[i][max(0, j-A)] or dp[i][max(0, j-B)]: dp[i+1][j] = 1
 
  # S になる組み合わせが存在しない。
  if not dp[-1][-1]:
    print("Impossible")
    return
 
  # 復元パート
  ab = "AB"
  ans = [""]*N
  current = S
  for i in reversed(range(N)):
    a_b_i = A_B[i]
    for j in range(2):
      if current-a_b_i[j] < 0: continue
      if dp[i][current-a_b_i[j]]:
        ans[i] = ab[j]
        current -= a_b_i[j]
        break
    
  print("".join(ans))
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
