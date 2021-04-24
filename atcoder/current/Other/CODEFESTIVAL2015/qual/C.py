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
        input = """5 7
1 0
3 0
5 0
2 0
4 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1000000000
5 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 0
100 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """3 11
5 2
6 4
7 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """6 92
31 4
15 9
26 5
35 8
97 9
32 3"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # i 番目の宿題を写すと Bi - Ai 分、得をする。
  # Bi - Ai の降順にソートして、その合計が sum(A) - T よりも大きくなるまで引き算する。
  N, T = map(int, input().split(" "))
  A_B = [[int(x) for x in input().split(" ")] for _ in range(N)]

  A_B.sort(key=lambda x: x[1]-x[0])
  dist = (-1)*T
  for i in range(N): dist += A_B[i][0]

  ans = 0
  if dist <= 0:
    print(ans)
    return
  for i in range(N):
    ans+=1
    dist-=A_B[i][0]-A_B[i][1]
    if dist <= 0:
      print(ans)
      return
  print(-1)
  return

resolve()


if __name__ == "__main__":
    unittest.main()
