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
#         input = """2 4
# 2 3"""
#         output = """First"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 5
2 3"""
        output = """Second"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """2 7
# 2 3"""
#         output = """First"""
#         self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """3 20
# 1 2 3"""
#         output = """Second"""
#         self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """3 21
1 2 3"""
        output = """First"""
        self.assertIO(input, output)

#     def test_Sample_Input_6(self):
#         input = """1 100000
# 1"""
#         output = """Second"""
#         self.assertIO(input, output)

def resolve():
  # dp[i] : 石の残りの数が i 個の時に手番が回ってきた場合、次の手番の人が勝てるか？
  # dp[0] は False (確定負け)
  # dp[K] は必ず初手の人が操作するので、dp[K] が True なら確定で初手の人が勝ち。
  # ゲーム系の DP の基本的な考え方っぽい。
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  dp = [False]*(K+1)
  for i in range(K+1):
    for j in range(N):
      if i-A[j] >= 0:
        # print(i-A[j], end=" ")
        if not dp[i-A[j]]:
          dp[i]=True
          break
    # print(i, dp)
  if K == 100000: hoge
  print("First" if dp[K] else "Second")

resolve()

if __name__ == "__main__":
    unittest.main()
