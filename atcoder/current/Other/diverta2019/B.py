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
1 1
2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 4
4 6
7 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1 1
1 2
2 1
2 2"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  #  N**3 くらいの計算までだったらなんとか間に合う気がする。N**4 だと6.25*10**6 だから厳しいか。
  # 0 コストでいける組み合わせを全て見つけた後、その集まりの接合部分を計算して、残りのコストを出す？
  N = int(input())
  x_y = [[int(x) for x in input().split(" ")] for _ in range(N)]

  p_q = set()
  for i in range(N):
    for j in range(N):
      if x_y[i][0] == x_y[j][0] and x_y[i][1] == x_y[j][1]: continue
      p_q.add((x_y[i][0]-x_y[j][0], x_y[i][1]-x_y[j][1]))

  ans = N
  for p, q in p_q:
    count=0
    for i in range(N):
      for j in range(N):
        if i == j: continue
        if (x_y[i][0]-p == x_y[j][0] and x_y[i][1]-q == x_y[j][1]):count+=1
    ans = min(ans, N - count)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
