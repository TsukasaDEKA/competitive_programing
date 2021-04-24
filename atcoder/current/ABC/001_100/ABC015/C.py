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
        input = """3 4
1 3 5 17
2 4 2 3
1 3 2 9"""
        output = """Found"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 3
89 62 15
44 36 17
4 24 24
25 98 99
66 33 57"""
        output = """Nothing"""
        self.assertIO(input, output)

def resolve():
  from itertools import product

  # 5**5 = 3125 なので全探索でいけそう。
  N, K = map(int, input().split(" "))
  T = [[int(x) for x in input().split(" ")] for _ in range(N)]

  targets = product(range(K), repeat=N)
  for target in targets:
    x = T[0][target[0]]
    for n in range(1, N):
      x^=T[n][target[n]]
    if x == 0:
      print("Found")
      return
  print("Nothing")

resolve()

if __name__ == "__main__":
    unittest.main()
