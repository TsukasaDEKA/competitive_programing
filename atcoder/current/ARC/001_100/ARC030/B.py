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
        input = """5 1
1 0 1 0 1
1 2
2 3
2 4
1 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 2
0 1 0
1 2
2 3"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  N, X = map(int, input().split(" "))
  X-=1
  H = [int(x) for x in input().split(" ")]
  # 開始点は移動しなくても取れるので、 宝石はなかったことにする。
  # 辺は必ず往復する。
  # 辺を 2 往復する必要はない。
  # 根以外の頂点は辺をただ一つ持つ。
  # 根以外で通らなくてはいけない頂点の個数 * 2 が答えになる。
  # 問題は、途中の経路をどうやって探すか。再帰的に解く？
  # 深さ優先探索をして、宝石に到達したら今まで通った頂点を入れる、
  # 末端まで到達したら全部捨てる、みたいにする。
  H[X] = 0
  route = [set() for _ in range(N)]
  for i in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    route[A].add(B)
    route[B].add(A)
  
  nexts = deque()
  nexts.append((X, 0))
  checked = [False]*N
  ans = set()
  while nexts:
    current, history = nexts.pop()

    if checked[current]: continue
    checked[current] = True
    if H[current]:
      for i in range(N):
        if history>>i&1: ans.add(i)
      history = 0

    for n in route[current]:
      if checked[n]: continue
      nexts.append((n, history|1<<n))


  print(len(ans)*2)

resolve()

if __name__ == "__main__":
    unittest.main()
