
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
        input = """6 6 3
1 3
2 4
1 4
4 6
5 6
1 5
2 6
1 5
3 6"""
        output = """Yes
Yes
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2 2
1 2
1 2
1 2
2 3"""
        output = """Yes
No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 1 1
1 2
1 2"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
  # 解説の方法を実装してみる。
  N, M, Q = map(int, input().split(" "))
  EDGES = [set() for _ in range(N)]

  for _ in range(M):
    x, y = [int(x)-1 for x in input().split(" ")]
    EDGES[y].add(x)
  
  Qs = [[int(x)-1 for x in input().split(" ")] for _ in range(Q)]
  bulk = 1<<10
  for i in range(0, Q, bulk):
    l = i
    r = min(Q, i+bulk)
    dp = [0]*N

    for j in range(len(Qs[l:r])):
      dp[Qs[l+j][0]] += 1<<j

    for v in range(N):
      for x in EDGES[v]:
        dp[v] |= dp[x]

    for j in range(len(Qs[l:r])):
      _, b = Qs[l+j]
      print("Yes" if (dp[b]>>j)&1 else "No")
    
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
