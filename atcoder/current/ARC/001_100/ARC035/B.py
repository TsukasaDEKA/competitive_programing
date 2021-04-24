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
        input = """2
20
10"""
        output = """40
1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
2
1
2
1
2"""
        output = """21
12"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """13
1
1
1
1
1
1
1
1
1
1
1
1
1"""
        output = """91
227020758"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # T1 が小さい順に解いていくのがペナルティ最小になる。
  from collections import Counter
  mod = 10**9+7
  N = int(input())
  A = sorted(Counter([int(input()) for _ in range(N)]).items())
  penalty = 0
  total_time = 0
  pattern = 1
  for time, count in A:
    penalty += count*(2*(total_time+time) + (count-1)*time)//2
    total_time += time*count
    for i in range(2, count+1):
      pattern *= i
      if pattern >= mod: pattern%=mod
  print(penalty, pattern, sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
