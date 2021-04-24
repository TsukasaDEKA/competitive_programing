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
        input = """2
1
7
15"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
1
4
2"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """300
57
121
244"""
        output = """NO"""
        self.assertIO(input, output)

def resolve():
  # N <= 300 程度なので、愚直にやっていっても解けそう。
  # ステップ数を数えながら DP？
  N = int(input())
  NG = set([int(input()) for _ in range(3)])

  if N in NG:
    print("NO")
    return

  field = [True]*(N+1)
  for ng in NG:
    if ng <= N: field[ng] = False

  count = 0
  while N > 0:
    for i in reversed(range(min(N, 3)+1)):
      if i==0:
        print("NO")
        return
      if field[N-i]:
        count+=1
        N-=i
        break

  print("YES" if count <= 100 else "NO")

resolve()

if __name__ == "__main__":
    unittest.main()
