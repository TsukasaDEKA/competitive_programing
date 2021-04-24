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
        input = """5 2 4
2
4
6
8
10"""
        output = """0.5 -1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """13 29 31
3
1
4
1
5
9
2
6
5
3
5
8
9"""
        output = """3.875 10.8173076"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5 1 2
34
34
34
34
34"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  # 最小の差は P 倍になる。また、平均は P 倍 した後 Q 追加される。
  # 平均を出すのは誤差が怖いので A*N で考える。
  N, A, B = map(int, input().split(" "))
  S = sorted([int(input()) for _ in range(N)])

  diff = S[-1] - S[0]
  if diff == 0:
    print(-1)
    return

  P = B/diff
  Q = (N*A-sum(S)*P)/N

  print(P, Q)

resolve()

if __name__ == "__main__":
    unittest.main()
