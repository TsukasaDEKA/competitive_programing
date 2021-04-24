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
1 2 3 4
3
1 2
3 4
2 4"""
        output = """11
12
16"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 1 1 1
3
1 2
2 1
3 5"""
        output = """8
4
4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
1 2
3
1 100
2 100
100 1000"""
        output = """102
200
2000"""
        self.assertIO(input, output)

from collections import Counter

def resolve():
  N = int(input())
  countA = Counter([int(x) for x in input().split(" ")])
  Q = int(input())

  sum_A = 0
  for a in countA.keys():
    sum_A += a*countA[a]

  for _ in range(Q):
    B, C = map(int, input().split(" "))
    if B in countA.keys():
      target_value = countA.pop(B)
      sum_A += (C - B) * target_value
      countA[C] += target_value
      print(sum_A)
    else:
      print(sum_A)


# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
