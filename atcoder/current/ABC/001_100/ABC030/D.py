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
        input = """6 4
5
2 3 1 2 6 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 1
100000000000000000000
2 3 4 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 1
1
2 3 4 5 3 2 4 5"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  # K <= N の時は愚直にシミュレートしても間に合う。
  # K >= N の時、愚直にやると間に合わない場合がある。
  # K >= N の時は必ず巡回が発生しているはずなので、それを利用する。
  N, a = map(int, input().split(" "))
  a -= 1
  K = int(input())
  B = [int(x)-1 for x in input().split(" ")]

  current = a
  if K <= N+10:
    for _ in range(K):
      current = B[current]
  else:
    steps = [-1]*N
    steps[current] = 0
    while steps[B[current]] < 0:
      steps[B[current]] = steps[current]+1
      current = B[current]
      K -= 1
    length = steps[current] - steps[B[current]] + 1
    K %= length
    for _ in range(K):
      current = B[current]

  print(current+1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()