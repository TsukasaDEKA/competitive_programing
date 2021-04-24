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
        input = """2 3 2
..#
###"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3 4
..#
###"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 2 3
##
##"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6 6 8
..##..
.#..#.
#....#
######
#....#
#....#"""
        output = """208"""
        self.assertIO(input, output)

import numpy as np
from itertools import product
from itertools import combinations

def resolve():
  H, W, K = map(int, input().split(" "))
  tasksH = []
  tasksH.append([])
  rangeH = range(H)
  for h in rangeH:
    tasksH.extend([list(x) for x in combinations(rangeH, h + 1)])

  tasksW = []
  tasksW.append([])
  rangeW = range(W)
  for w in rangeW:
    tasksW.extend([list(x) for x in combinations(rangeW, w + 1)])


  tasks = [list(x) for x in product(tasksH, tasksW)]

  C = []
  for h in range(H):
    C.append([x == "#" for x in list(input()) ])
  C = np.array(C)

  result = 0
  for task in tasks:
    if np.sum(C[np.ix_(task[0], task[1])]) == K:
      result += 1
  print(result)

if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
