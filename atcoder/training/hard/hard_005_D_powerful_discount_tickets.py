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
        input = """3 3
2 13 8"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
1 9 3 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 100000
1000000000"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """9500000000"""
        self.assertIO(input, output)

from heapq import heapify, heappop, heappush

def resolve():
  N, M = map(int, input().split(" "))
  A = [(-1)*int(x) for x in input().split(" ")]
  heapify(A)

  for _ in range(M):
    max_A = (-1)*heappop(A)
    heappush(A, (-1)*(max_A//2))
  
  print((-1)*sum(A))

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
