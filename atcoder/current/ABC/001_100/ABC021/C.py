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
        input = """7
1 7
8
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """7
1 7
9
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6
4 7"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  # 最短経路の本数・・・幅優先探索？
  # なんか DP っぽい
  # 通ってきた経路を復元する？
  # 幅優先探索をして、距離が一緒ならそこまで到達するまでのパターン数を足すようにやっていく。
  from collections import deque

  mod = 10**9+7
  inf = 10**18+1

  N = int(input())
  A, B = [int(x)-1 for x in input().split(" ")]
  M = int(input())

  ROUTE = [set() for _ in range(N)]
  for i in range(M):
    X, Y = [int(x)-1 for x in input().split(" ")]
    ROUTE[X].add(Y)
    ROUTE[Y].add(X)

  next_ = deque()
  next_.append(A)
  step = [0]*N
  pattarn = [0]*N
  pattarn[A] = 1
  checked = [False]*N
  checked[A] = True
  while next_:
    c = next_.popleft()

    for n in ROUTE[c]:
      if checked[n]:
        if step[n] == step[c]+1:
          pattarn[n] += pattarn[c]
        continue
      pattarn[n] = pattarn[c]
      checked[n] = True
      step[n] = step[c]+1
      next_.append(n)
  print(pattarn[B]%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
