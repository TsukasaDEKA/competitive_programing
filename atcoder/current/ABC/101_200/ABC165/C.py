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
        input = """3 4 3
1 3 3 100
1 2 2 10
2 3 2 10"""
        output = """110"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """4 6 10
2 4 1 86568
1 4 0 90629
2 3 0 90310
3 4 1 29211
3 4 3 78537
3 4 2 8580
1 2 1 96263
1 4 2 2156
1 2 0 94325
1 4 3 94328"""
        output = """357500"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """10 10 1
1 10 9 1"""
        output = """1"""
        self.assertIO(input, output)

from itertools import combinations_with_replacement

def resolve():
  N, M, Q = map(int, input().split(" "))
  a_b_c_d_list = [[int(j)for j in input().split(" ")] for i in range(Q)]

  ans_max = 0
  for combination in combinations_with_replacement(list(range(1, M+1)), N):
    ans = 0
    for a, b, c, d in a_b_c_d_list:
      if combination[b-1] - combination[a-1] == c: ans += d
    ans_max = max(ans_max, ans)
  print(ans_max)

# if __name__ == "__main__":
#     resolve()

if __name__ == "__main__":
    unittest.main()