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
        input = """4 4
1 2
1 3
2 4
3 4
3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
1 2
1 3
2 4
3 4
4
3 4
1 2
2 4
2 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 12
2 3
4 6
1 2
4 5
2 6
1 5
4 5
1 3
1 2
2 6
2 3
2 5
5
3 5
1 4
2 6
4 6
5 6"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  # inf = 10**10+1
  # 愚直でぎり間に合いそう
  N, M = map(int, input().split(" "))
  A_B= [[int(x)-1 for x in input().split(" ")] for _ in range(M)]
  K = int(input())
  C_D= [[int(x)-1 for x in input().split(" ")] for _ in range(K)]

  dishes = [False]*N
  ans = 0
  for t in range(2**K):
    dishes = [False]*N
    for i in range(K):
      dishes[C_D[i][t>>i&1]] = True
    count = 0
    for A, B in A_B:
      if dishes[A] and dishes[B]: count+=1
    ans = max(ans, count)
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
