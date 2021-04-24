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
        input = """4
2 2 1 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
1 1 1 1 1 1 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
3 3 3 2 2 1 1"""
        output = """17"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2
3 3"""
        output = """3"""
        self.assertIO(input, output)

import collections

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  setA = set(A)
  listA = sorted(list(setA))
  collectionA = collections.Counter(A)

  result = listA[-1]
  collectionA[listA[-1]] -= 1

  if collectionA[listA[-1]] == 0:
    listA.pop()

  for list_a in listA:
    collectionA[list_a] *= 2

  for i in range(N - 2):
    result += listA[-1]
    collectionA[listA[-1]] -= 1
    if collectionA[listA[-1]] == 0:
      listA.pop()

  print(result)


resolve()

if __name__ == "__main__":
    unittest.main()
