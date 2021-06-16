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
1 2
2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2
2 3
3 4
3 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
1 2
1 3
2 4
4 5
4 6
3 7
7 8
8 9
8 10"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """31
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15
8 16
8 17
9 18
9 19
10 20
10 21
11 22
11 23
12 24
12 25
13 26
13 27
14 28
14 29
15 30
15 31"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  # 木構造
  # スコアは最大で N になる。
  # 葉と葉をつなげるとスコアが最大になりそう。
  # 葉に高さを記録していくといけるかも。
  # どこを根にするかで結果が変わる。
  # 次数が 1 のノードを根にすると困った事になりそう。
  # ↑の考え方だと木の構造次第で良い結果がでなさそうなので考え直す。
  # 深さ優先探索で、戻り際に以下の処理をする。
  # そのノードの今までに見た子の高さの最大値 + 今見てきた子の最大高さを計算して、スコアを更新
  # そのノードの今までに見た子の高さの最大値を更新
  # 深さ優先探索だと難しい？
  # なんかいける気がするけど・・・
  # 直前の深さを記録しておいて、前に進むタイミングで 0 に戻す？
  # 木の直径を求めるアルゴリズムってのがあるらしい。
  # https://algo-logic.info/tree-diameter/
  from collections import deque
  inf = 10**18+1

  N = int(input())
  PATH = [set() for _ in range(N)]
  # 戻りの時に処理する場合、0-index だとおかしくなるので、1-index でやる。
  for i in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    PATH[a].add(b)
    PATH[b].add(a)
  
  def dfs(N, path, start):
    most_far_i = 0
    diff = 0

    step = [0]*N
    checked = [False]*(N)
    checked[start] = True
    nexts = deque([start])
    while nexts:
      current = nexts.pop()
      if step[current] > diff:
        diff = step[current]
        most_far_i = current

      for n in PATH[current]:
        if checked[n]: continue
        checked[n] = True
        step[n] = step[current]+1
        nexts.append(n)
    return diff, most_far_i
  
  _, i = dfs(N, PATH, 0)
  ans, _ = dfs(N, PATH, i)
  print(ans+1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
