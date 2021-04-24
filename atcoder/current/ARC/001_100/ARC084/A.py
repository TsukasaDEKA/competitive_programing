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
        input = """2
1 5
2 4
3 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 1 1
2 2 2
3 3 3"""
        output = """27"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """6
# 3 14 159 2 6 53
# 58 9 79 323 84 6
# 2643 383 2 79 50 288"""
#         output = """87"""
#         self.assertIO(input, output)


    def test_Sample_Input_4(self):
        input = """6
2 3 6 14 53 159
6 9 58 79 84 323
2 50 79 288 383 2643"""
        output = """87"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """6
1 2 3 4 5 6
5 5 8 9 10 11
6 6 6 6 6 6"""
        output = """24"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  B = sorted([int(x) for x in input().split(" ")])
  C = sorted([int(x) for x in input().split(" ")])

  # A[i] < B[j] < C[k] になる i, j, k が条件。
  # A[i] を選ぶ => A より大きい B の最小値 B[j] を二分探索で選ぶ  => B より大きい C の最小値 C[k] を二分探索で選ぶとすると
  # 答えは (N-j)+(N-k) で、計算量は O(N*logN*logN) で間に合わないかも？
  # i = j = k = 0 から初めて、尺取じゃないけど C[k] > B[j] になる j の最小値を求めて、B と A でも同じことをやって・・・ってすれば O(3*N)
  # j を選んだ時の i の個数の累積和を取っておく？
  # O(4*N) になっちゃうけど間に合うだろ多分
  integral_ixj = [0]*(N+1)
  i = j = 0
  for j in range(N):
    if i+1 < N:
      while A[i+1] < B[j]:
        i+=1
        if not i+1 < N: break
    if A[i] < B[j]: 
      integral_ixj[j+1] = integral_ixj[j] + i + 1

  ans=0
  j = k = 0
  for k in range(N):
    if j+1 < N:
      while B[j+1] < C[k]:
        j+=1
        if not j+1 < N: break
    if B[j] < C[k]:
      ans+=integral_ixj[j+1]
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
