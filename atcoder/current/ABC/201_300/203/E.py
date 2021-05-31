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
        input = """2 4
1 1
1 2
2 0
4 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
1 1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  from collections import defaultdict

  # 2*N 分のマスがあるのが辛い。
  # 正面に黒のポーンがある時、白のポーンは消滅する。
  # 斜め方向に黒のポーンがある時、そっち方向に白のポーンが増える。
  N, M = map(int, input().split(" "))
  black = defaultdict(list)
  for _ in range(M):
    X, Y = [int(x) for x in input().split(" ")]
    black[X].append(Y)
  
  black_i = sorted(black.keys())
  for b in black_i:
    black[b].sort()
  
  white = set()
  white.add(N)
  for b in black_i:
    # 追加と削除は遅延で行う。
    delete = set()
    add = set()
    tar = black[b]
    for t in tar:
      # 右下に黒がいる場合
      if t-1 in white or t+1 in white: add.add(t)
      # 正面に黒がいる場合
      if t in white and t not in add: delete.add(t)

    # 反映処理
    # 先に delete 処理から行う。
    for d in delete: white.remove(d)
    for a in add: white.add(a)
    if len(white) == 0: break
  print(len(white))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
