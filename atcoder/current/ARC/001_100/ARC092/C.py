import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff = None
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
2 0
3 1
1 3
4 2
0 4
5 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
0 0
1 1
5 2
2 3
3 4
4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
2 2
3 3
0 0
1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
0 0
7 3
2 2
4 8
1 6
8 5
6 9
5 4
9 1
3 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """5
0 0
1 1
5 5
6 6
7 7
2 2
3 3
4 4
8 8
9 9"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  # 解説を読んだら別解の方で解いていたので、想定解の方でも実装してみる。
  # 要素数が少ないので、多少計算量が嵩むやり方でも通りそう。
  N = int(input())
  R = sorted([list(map(int, input().split(" "))) for _ in range(N)], key=lambda x: x[1], reverse=True)
  B = sorted([list(map(int, input().split(" "))) for _ in range(N)])

  checked_red = [False]*N
  ans = 0
  for b_x, b_y in B:
    for i in range(N):
      if checked_red[i]: continue
      r_x, r_y = R[i]
      if r_x < b_x and r_y < b_y:
        ans+=1
        checked_red[i] = True
        break
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
