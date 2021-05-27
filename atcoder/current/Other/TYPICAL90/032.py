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

    def test_入力例_1(self):
        input = """3
1 10 100
10 1 100
100 10 1
1
1 2"""
        output = """111"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2
1 3
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 10 100
10 1 100
100 10 1
0"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  from itertools import permutations
  # 10! = 3628800 で、パターンの計算に最大で 10 回の計算が行われる。
  # 3628800*10 なので多分間に合う。
  # 相性問題に関しては set で持っておく。
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  M = int(input())
  BAD_PAIR = [set() for _ in range(N)]
  for _ in range(M):
    X, Y = [int(x)-1 for x in input().split(" ")]
    BAD_PAIR[X].add(Y)
    BAD_PAIR[Y].add(X)

  ans = inf
  for tar in permutations(list(range(N)), N):
    temp = A[tar[0]][0]
    for i in range(1, N):
      if tar[i-1] in BAD_PAIR[tar[i]]: break
      temp += A[tar[i]][i]
    else:
      ans = min(ans, temp)
  if ans == inf:
    print(-1)
    return
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
