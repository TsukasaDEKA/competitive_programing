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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)


from math import gcd
from functools import reduce
from itertools import product

def resolve():
  N, M = map(int, input().split(" "))
  H = [int(x) for x in input().split(" ")]

  AB = []
  for i in range(M):
    AB.append([int(x)-1 for x in input().split(" ")])

  result = [True] * N
  for ab in AB:
    if H[ab[0]] > H[ab[1]]:
      result[ab[1]] = False
      continue
    if H[ab[1]] > H[ab[0]]:
      result[ab[0]] = False
      continue
    if H[ab[1]] == H[ab[0]]:
      result[ab[0]] = False
      result[ab[1]] = False
      continue

  print(result.count(True))
  # for h_index in range(0, N):
  #   flag = True
  #   for ab in AB:
  #     if ab[0] == h_index+1 or ab[1] == h_index+1:
  #       if H[ab[0]-1] > H[h_index] or H[ab[1]-1] > H[h_index] or H[ab[0]-1] == H[ab[1]-1]:
  #         flag = False
  #         continue

  #   if flag:
  #     count += 1

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()