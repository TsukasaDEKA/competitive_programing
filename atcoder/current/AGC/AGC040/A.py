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
        input = """<>>"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """<>>><<><<<<<>>><"""
        output = """28"""
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
  i = j = k = 0
  for k in range(N):
    if j+1 < N:
      while B[j+1] < C[k]:
        j+=1
        if not j+1 < N: break

    if i+1 < N:
      while A[i+1] < B[j]:
        i+=1
        if not i+1 < N: break
    ans+=(i+1)*(j+1)
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
