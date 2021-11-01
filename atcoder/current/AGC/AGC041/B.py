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
        input = """6 1 2 2
2 1 1 3 0 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 1 5 2
2 1 1 3 0 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 4 8 5
7 2 3 6 1 6 5 4 6 5"""
        output = """8"""
        self.assertIO(input, output)



debug = False
def resolve():
  from itertools import accumulate # 累積和作るやつ
  # P 番目の問題のスコアが X の時、スコア X の他の問題も問題セットに含まれる可能性を持つ。
  # 考え方は簡単なんだけど場合分けが厄介。
  inf = 10**18+1
  N, M, V, P = map(int, input().split(" "))
  # bisect を使いたいので昇順で考える。
  A = sorted([int(x) for x in input().split(" ")])

  # 残りの投票で現状 P 番目の問題の点数を超えられるかどうかを考える。
  accA = [0]+list(accumulate(A))
  if debug: print(A,accA, A[-P])
  for i in range(N-P):
    # a: i 番目が取りうる最大値。
    a = A[i]+M
    # 現時点での A[-P] よりも a が小さい場合、その問題は問題セットに含まれる可能性がない。
    if a < A[-P]: continue

    # 末尾から P 番目の問題のインデックス。この問題より左側に分散投票した時に、i 番目の問題が同率 1 位になれるか考える。
    index = N-P

    # i 番目以前の問題に全員が投票し、残りをいい感じに散らした場合に A[i] が同率トップを取れるかどうかを考える。
    v = V-(P-1)-i
    if debug: print(i, a, v*M, a*(index-i+1), (accA[index+1]-accA[i]), a*(index-i) - (accA[index+1]-accA[i]))
    if v*M <= a*(index-i+1) - (accA[index+1]-accA[i]):
      print(N-i)
      return
  print(P)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  # debug = True
  unittest.main()