
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
  from collections import deque
  inf = 10**18+1
  # ダブリングを使う？
  # 親が複数の場合があるので、それは難しい。
  # 子孫を全部ノードに持ってたら早いのに！
  # 小課題は毎回探索していっても大丈夫そう。
  N, M, Q = map(int, input().split(" "))
  EDGES = [set() for _ in range(N)]
  for _ in range(M):
    x, y = [int(x)-1 for x in input().split(" ")]
    EDGES[x].add(y)
  
  for _ in range(Q):
    a, b = [int(x)-1 for x in input().split(" ")]
    nexts = deque([a])
    checked = [x==a for x in range(N)]
    while nexts:
      current = nexts.pop()
      if current == b:
        print("Yes")
        break
      for n in EDGES[current]:
        if checked[n]: continue
        checked[n] == True
        nexts.append(n)
        if n == b: break
    else:
      print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
