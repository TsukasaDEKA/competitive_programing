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
        input = """5 3"""
        output = """1 10
8 12
13 20
11 14
2 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 -10"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  # M >= 0の場合を考える。
  # 例えば、N = 5, M = 1 の時、
  # (2, 3), (5, 6), (8, 9), (11, 12) のように一つ開けの階段のように作る。
  # 最後の 1 つを例えば (7, 14) のようにすると、
  # 青木くんは (2, 3), (5, 6), (7, 14) を選んで 3 個、
  # 高橋くんは (2, 3), (5, 6), (8, 9), (11, 12) を選んで 4 個
  # 4 - 3 = 1 == M になる。

  # 最後の一つをいれる場所でコントロールできる？
  # 最後の 1 つを (1, 14) のようにすると、
  # 青木くんは (1, 14) のみで 1 個、高橋くんは (2, 3), (5, 6), (8, 9), (11, 12) の 4 個で
  # 4-1 の 3 個になる。

  # 最後の 1 つを (4, 14) のようにすると、
  # 青木くんは (2, 3), (4, 14) で 2 個、高橋くんは (2, 3), (5, 6), (8, 9), (11, 12) の 4 個で
  # 4-2 の 2 個になる。

  # 最後の 1 つを (10, 14) のようにすると、
  # 青木くんは (2, 3), (5, 6), (8, 9), (10, 14) で 4 個、高橋くんは (2, 3), (5, 6), (8, 9), (11, 12) の 4 個で
  # 4-4 の 0 個になる。

  # M が負の場合を考える。
  # 高橋くんが青木くんのやつより多く取れるパターンが思いつかない。
  # M が負の場合は -1 にしてみる？

  N, M = map(int, input().split(" "))
  # 青木くんは必ず最初の一つは取ることになる。
  # また、高橋くんは青木くんが最初にとった区間を取るとその時点で他に取れない物が出てくるので、
  # 差の最大値は N - 2 になる。
  # N == 1 の時だけ上手く処理できないので、ここで解を出しておく。
  if N == 1 and M == 0:
    print(1, 2)
    return

  if N - M < 2 or M < 0:
    print(-1)
    return
  ans = [[2+3*i, 3+3*i] for i in range(N-1)]
  ans.append([ans[N - M - 2][0]-1, ans[-1][1]+1])
  for a in ans:
    print(*a)

resolve()

if __name__ == "__main__":
    unittest.main()
