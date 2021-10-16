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
        input = """7
3 6
1 2
3 1
7 4
5 7
1 4"""
        output = """Fennec"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
3 6
3 1
7 2
5 7
1 4
4 2"""
        output = """Fennec"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 4
4 2
2 3"""
        output = """Snuke"""
        self.assertIO(input, output)

def resolve():
  # 木構造だとすると、親を先に取った場合、その親を根とする部分木はそのプレイヤーだけが使える状態になる。
  # そのため、1 => N までの最短経路上をお互いにその経路を辿りながら塗っていくのが最善になる。
  # 最初に最短経路を求める。
  # 次にその最短経路をお互いに塗り潰す処理を入れていく。
  # あとは愚直にシミュレートに近いことをすれば OK
  # 最短経路を求める処理が厄介。

  from collections import deque
  N = int(input())
  EDGES = [set() for _ in range(N)]
  for _ in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    EDGES[a].add(b)
    EDGES[b].add(a)

  # 最短経路を求める。
  route = [N-1]
  found_N = False
  nexts = deque([0])
  checked = [False]*N
  checked[0] = True
  while nexts:
    current = nexts.pop()
    if current < 0:
      if found_N and -current in EDGES[route[-1]]:
        route.append(-current)
      continue
    
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      if n == N-1: found_N = True
      if found_N: continue
      nexts.append(-n)
      nexts.append(n)

  route.append(0)

  # 上記で求めた最短経路を元に tree を作る。
  checked = [False]*N
  N_route = len(route)
  white_count = N_route//2
  # N ~ 最短経路の半分まで白で、残りを黒で塗る。
  for i in range(N_route):
    checked[route[i]] = True
    if i < N_route//2:
      nexts.append(route[i])

  while nexts:
    current = nexts.pop()
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      white_count+=1
      nexts.append(n)

  print("Fennec" if N > 2*white_count else "Snuke")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()