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

    def test_入力例1(self):
        input = """3 2 1
9 5
3 1
8 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 4 100
999 999 999 999
999 999 999 999
999 999 999 999
999 999 999 999"""
        output = """999"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3 4 5
700 198 700 198
198 700 198 700
700 198 700 198"""
        output = """198"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  dx = [1, 0]
  dy = [0, 1]
  # D - そのマスにたどり着くまでの最小ステップ数が偶数だったら最終的にそのマスに戻ってくることができる。
  # 幅優先探索しながら最大値を探していく。
  R, C, D = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(R)]

  next_ = deque()
  next_.append((0, 0))
  step = [[0]*C for _ in range(R)]
  checked = [[False]*C for _ in range(R)]
  checked[0][0] = True
  ans = A[0][0] if D%2==0 else 0
  while next_:
    x, y = next_.popleft()
    for i in range(2):
      x_ = x+dx[i]
      y_ = y+dy[i]
      if x_ < R and y_ < C:
        if checked[x_][y_]: continue
        checked[x_][y_] = True
        step[x_][y_] = step[x][y]+1
        if (D - step[x_][y_])%2==0 and D >= step[x_][y_]:
          ans = max(ans, A[x_][y_])
        next_.append((x_, y_))
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
