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
        input = """1 2
80 84"""
        output = """84"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 4
37 29 70 41
85 69 76 50
53 10 95 100"""
        output = """250"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 2
31000000 41000000
59000000 26000000
53000000 58000000
97000000 93000000
23000000 84000000
62000000 64000000
33000000 83000000
27000000 95000000"""
        output = """581000000"""
        self.assertIO(input, output)

def resolve():
  from itertools import combinations

  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  ans = 0
  for p in combinations(list(range(M)), 2):
    temp = 0
    for i in range(N):
      temp += max(A[i][p[0]], A[i][p[1]])
    ans = max(ans, temp)

  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()