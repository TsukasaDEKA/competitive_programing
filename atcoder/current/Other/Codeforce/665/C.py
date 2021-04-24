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
1
8
6
4 3 6 6 2 9
4
4 5 6 7
5
7 5 2 2 4"""
        output = """YES
YES
YES
NO"""
        self.assertIO(input, output)

from math import gcd

def resolve():
  loop_n = int(input())
  for _ in range(loop_n):
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    if N == 1:
      print("YES")
      continue
    
    minA = min(A)
    sortedA = sorted(A)

    unmovable = [x%minA!=0 for x in A]
    breaked = False
    for i, a in enumerate(A):
      if a != sortedA[i] and unmovable[i]:
        print("NO")
        breaked = True
        break
    if not breaked:
      print("YES")

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
  unittest.main()