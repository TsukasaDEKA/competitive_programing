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
        input = """10 10 3
1 5
3 6
7 10
5 8
4 4
1 4
2 9
1 3
1 1
4 5
1 6
2 7
10 1"""
        output = """2
4
8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10 10 4
1 2
2 4
3 6
4 8
5 10
9 10
7 8
5 6
3 5
1 3
10 1
3 8
2 4
1 3"""
        output = """10
4
2
2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """314159265 10 1
1 10000
500 12031
1414 113232
111111 777777
666661 23423423
12345678 123456789
111111111 314159265
112334 235235235
1 223445
314 1592
1 314159265"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
  # Li ~ Ri の間に T が含まれているのであれば、それを実行するのが合理的。
  # D * K = 10**(4+2) 程度だったら多分間に合う。
  # 愚直にやってみる。
  N, D, K = map(int, input().split(" "))
  L_R = [[int(x)-1 for x in input().split(" ")] for _ in range(D)]
  S_T = [[int(x)-1 for x in input().split(" ")] for _ in range(K)]

  dates = [None]*K
  for k in range(K):
    if dates[k] is not None: continue
    start, goal = S_T[k]
    for d in range(D):
      L, R = L_R[d]
      if L <= start and start <= R:
        if L <= goal and goal <= R:
          dates[k] = d + 1
          break

        if goal < L:
          start = L
        else:
          start = R

  print(*dates, sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
