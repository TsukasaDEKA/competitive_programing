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

    def test_入力例_1(self):
        input = """3 7 20
1 2 4"""
        output = """3 6 11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3 100
1 1 1"""
        output = """34 33 33"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 10006 10
10000 3 2 1 0 0"""
        output = """10 0 0 0 0 0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 78314 1000
53515 10620 7271 3817 1910 956 225"""
        output = """683 136 93 49 24 12 3"""
        self.assertIO(input, output)

from heapq import heappop, heappush

def resolve():
  K, N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  A_N = [a/N for a in A]
  B = [0]*K

  # 後でどれくらい余った分を割り振るのに使う。
  diff = M
  errors = []
  for i in range(K):
    B[i] = int((A[i]/N)*M)
    diff-=B[i]
    heappush(errors, ((N*B[i]-M*A[i])/(M*N), i))

  # 余った分を愚直に割り振っていく。
  # 誤差が大きい順に 1 入れていく。
  # 誤差順の取り出しは優先度付きキューを使う。
  for _ in range(diff):
    _, i = heappop(errors)
    B[i]+=1

  print(*B)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
