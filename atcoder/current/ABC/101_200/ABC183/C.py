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

    def test_Sample_Input_1(self):
        input = """4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0"""
        output = """24"""
        self.assertIO(input, output)

from itertools import permutations

def resolve():
  inf = 10**10+1
  N, K = map(int, input().split(" "))
  T = [[int(x) for x in input().split(" ")] for _ in range(N)]

  l = list(range(1, N))
  patterns = permutations(l, len(l))
  ans = 0
  for pattern in patterns:
    time = 0
    from_ = 0
    for to in pattern:
      time += T[from_][to]
      from_ = to
    
    time += T[from_][0]
    if time == K: ans+=1
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
