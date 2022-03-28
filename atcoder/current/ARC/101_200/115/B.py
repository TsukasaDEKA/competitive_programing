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
        input = """3
4 3 5
2 1 3
3 2 4"""
        output = """Yes
2 0 1
2 1 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
4 3 5
2 2 3
3 2 4"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter 
  N = int(input())
  C = [list(map(int, input().split(" "))) for _ in range(N)]
  base = C[0]
  diff = [[c-b for b, c in zip(base, line)] for line in C]
  b = C[0]
  a = [0]*N
  for i in range(N):
    count = Counter(diff[i])
    if len(count.values()) != 1:
      print("No")
      return
    a[i] = list(count.keys())[0]
  min_a = min(a)
  a = [x-min_a for x in a]
  b = [x+min_a for x in b]
  print("Yes")
  print(*a, sep=" ")
  print(*b, sep=" ")


resolve()

if __name__ == "__main__":
    unittest.main()
