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
        input = """4"""
        output = """1
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7"""
        output = """1
2
4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # Bit DP ?
  # 1 ~ N の内、1 ~ X までの合計 (sum_X) がギリギリ N 以上の時、 sum_X - N < X になる。
  # そうならない場合は X-1 までの和で N を超えているはず。
  # また、sum_X - N < X なので、 sum_X - N なる数字を sum_X から除外することで、N と等しくなり、高橋くんの要望と一致することになる。
  # また、X-1 までの和が N を超えていないことから、X は必ず必要になることがわかる。
  # 以上のことから sum(1, 2, ... X) がギリギリ N を超える X を見つけ出し、sum(1, 2, ... X) - N だけ出力しないようにすることで答えが出る。
  # 1 ~ X までの合計は X(X+1)/2 になり、これは N より大きく、X-1 までの和が (X-1)X/2 < N であることを考えると
  # X の範囲はせいぜい 1 ~ sqrt(2*N) 程度になって N <= 10**7 であることを考えるとそんなに広くない。 10**4 未満。
  # 二分探索等をする必要はなさそう。
  N = int(input())

  sum_X = 0
  for x in range(1, N+1):
    sum_X += x
    if sum_X >= N: break

  ans = list(range(1, x+1))
  if sum_X != N: del ans[sum_X-N-1]
  print(*ans, sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
