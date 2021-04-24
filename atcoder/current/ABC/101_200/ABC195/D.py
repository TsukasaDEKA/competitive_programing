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
        input = """3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3"""
        output = """20
0
9"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M, Q = map(int, input().split(" "))
  W_V = sorted([list(map(int, input().split(" "))) for _ in range(N)], key=lambda x: x[1], reverse=True)
  X = [int(x) for x in input().split(" ")]

  can_use = [[] for _ in range(N)]
  for m in range(M):
    for i in range(N):
      if W_V[i][0] <= X[m]:
        can_use[i].append((X[m], m))

  can_use = [sorted(x) for x in can_use]
  # N, M, Q は 50 以下
  for _ in range(Q):
    L, R = [int(x)-1 for x in input().split(" ")]
    ans = 0
    used = [i >= L and i <= R for i in range(M)]

    # 商品をループ
    for i in range(N):
      # 入る箱でループ
      for _, m in can_use[i]:
        if not used[m]:
          ans += W_V[i][1]
          used[m] = True
          break
    print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
