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
        input = """4
2 4
4 3
9 3
100 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
8 20
1 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
10 1
2 1
4 1
6 1
8 1"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  arm_ranges = [None] * N
  # 腕の動く範囲の最小値と最大値を記録する。
  for i in range(N):
    X, L = map(int, input().split(" "))
    arm_ranges[i] = (X-L, X+L)
  # 腕の動く範囲の最大値が小さい順でソートする。
  arm_ranges = sorted(arm_ranges,  key=lambda x: x[1])

  # 腕の動く範囲の最小値が前に選んだものの最大値よりも大きかったら取る、でなければ取らないというのを繰り返す。
  ans = 1
  recent_selected = arm_ranges[0]
  for arm_range in arm_ranges[1:]:
    if recent_selected[1] <= arm_range[0]:
      ans += 1
      recent_selected = arm_range

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
