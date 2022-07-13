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
3 3
30 10 40
20 50 60
60 60 50
5 2
1 1000000000
500000000 1000000000
1 1000000000
500000000 1
1 1000000000"""
        output = """Case #1: 110
Case #2: 4999999996"""
        self.assertIO(input, output)

def resolve():
  # シミュレートしていこう。
  from collections import deque
  T = int(input())

  for t in range(1, T+1):
    # dp っぽい。
    # 上下のどっちから入って、どっちから出るのかを計画すればよい。
    N, K = map(int, input().split(" "))

    left_p, right_p = 0, 0
    left_count, right_count = 0, 0
    for i in range(N):
      A = sorted([int(x) for x in input().split(" ")])
      current_l_p, current_r_p = A[0], A[-1]
      diff = abs(current_r_p-current_l_p)
      # 左から出る場合の挙動。
      temp_l_count = min(abs(right_p-current_r_p)+diff+right_count, abs(left_p-current_r_p)+diff+left_count)
      # 右から出る場合の挙動。
      temp_r_count = min(abs(right_p-current_l_p)+diff+right_count, abs(left_p-current_l_p)+diff+left_count)

      left_count, right_count = temp_l_count, temp_r_count
      left_p, right_p = current_l_p, current_r_p
    print("Case #{0}: {1}".format(t, min(left_count, right_count)))

resolve()

if __name__ == "__main__":
  unittest.main()