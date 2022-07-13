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
        input = """5 5
1 2
1 3
3 2
5 2
4 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1
1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 18
7 2
1 6
5 2
1 3
7 6
5 3
5 6
5 4
1 7
2 6
3 4
5 1
4 7
4 6
5 7
3 2
4 2
1 4"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # グラフ構築の段階で頂点 i が持つ隣接点の個数はわかる。
  # 自分より小さい隣接点の個数が、0, 1, 2~ なのかはソートされてればすぐわかるけど、
  # 愚直にソートすると最悪 N*NlogN かかる。
  # プライオリティキューを使うのが良さげ
  from heapq import heappop, heappush

  N, M = map(int, input().split(" "))
  ADA = [[] for _ in range(N)]
  for i in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    heappush(ADA[A], B)
    heappush(ADA[B], A)

  ans = 0
  for i in range(N):
    count = 0
    while count <= 1 and ADA[i]:
      ada = heappop(ADA[i])
      if ada > i: break
      count+=1

    if count == 1:
      ans += count
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()