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
        input = """6
123 223 123 523 200 2000"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
199 100 200 400 300 500 600 200"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  # 100 の位の偶奇と下二桁で集計する。
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  agg = [[0]*2 for _ in range(100)]
  for a in A:
    head, tail = (a//100)%2, a%100
    agg[tail][head] += 1

  ans = 0
  for i in range(2):
    for j in range(100):
      val = agg[j][i]
      ans += val*(val-1)//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
