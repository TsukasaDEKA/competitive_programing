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
        input = """5 3"""
        output = """5
4 3
1 2
3 1
4 5
2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 8"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  # 最短距離が 2 であるような頂点対は最大で (N-1)*(N-2)/2 個。(星状に配置した時。)
  # それ以下であれば確実に実現できるかどうかを考える。
  # 全部の頂点に辺を張ると 0 個
  # 任意の 2 頂点を選んで辺を削除すると 1 個になる。
  # 連結を維持したまま辺を削除すると 2 個に増える。
  # N = 5 の場合、1, 2, 3, 4, 5, 6 までは実現可能。
  # 解き方:
  # 一旦全部結合する。
  # その内、頂点 1 から伸びている辺は維持する。
  # 頂点 2 から伸びている i > 2 の辺を順に削除していく。
  # 削除する辺がなくなったら頂点 3 から伸びてる辺を削除する。
  N, K = map(int, input().split(" "))
  if K > (N-1)*(N-2)//2:
    print(-1)
    return

  ans = [(1, x) for x in range(2, N+1)]
  for i in range(2, N):
    for j in range(min(i+1+K, N+1), N+1):
      ans.append((i, j))
    K = max(K-(N-i), 0)
  print(len(ans))
  for i, j in ans:
    print(i, j)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()