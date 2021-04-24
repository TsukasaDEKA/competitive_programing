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
        input = """3
1 0 0"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 後ろから決めていくと一意に決まるので、N 回の処理になる。
  # それぞれの足し算は N+N/2+...+N/N = logN + C 回行うことになるので、大体 O(NlogN) (NlogN < 4 * 10**6) なので間に合うはず。
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  ans = set()
  boxes = [0] * (N)
  ball_count = 0
  # 逆順で箱に入れるかどうかを定めていく。
  # 1-index じゃないと都合が悪いので調整
  for i in reversed(range(1, N+1)):
    sum_balls = 0
    # 既に位置が確定したボールを条件に合わせて集計
    temp_i = 2*i
    while temp_i < N+1:
      sum_balls += boxes[temp_i-1]
      temp_i += i
    # ボールを箱に入れるかどうか決める。
    if (sum_balls)%2 != A[i-1]:
      boxes[i-1] = 1
      ans.add(i)
      ball_count+=1

  if ball_count:
    print(ball_count)
    print(*ans)
  else:
    print(0)
# resolve()

if __name__ == "__main__":
    unittest.main()
