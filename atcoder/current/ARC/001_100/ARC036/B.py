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
        input = """6
4
5
1
6
9
7"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """7
90
70
50
30
20
10
5"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """7
1
2
3
4
5
6
7"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """7
1
2
1
2
3
2
1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """1
1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 登り始めたら山開始で降りきったら山終了
  N = int(input())
  H = [int(input()) for _ in range(N)]

  ans = 1
  count = 1
  up = True
  for i in range(1, N):
    if up:
      count += 1
      if H[i-1] > H[i]:
        up = False
    else:
      if H[i-1] > H[i]:
        count += 1
      else:
        up = True
        count = 2
    ans = max(ans, count)
  print(ans)

resolve()


if __name__ == "__main__":
    unittest.main()
