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
        input = """4 2
3 1 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20 12
7 11 10 1 7 20 14 2 17 3 2 5 19 20 8 14 18 2 10 10"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  inf = 10**18+1
  N, X = map(int, input().split(" "))
  X -= 1
  A = [int(x)-1 for x in input().split(" ")]

  nexts = deque()
  nexts.append(X)
  checked = [False]*N
  checked[X] = True
  while nexts:
    current = nexts.pop()
    if checked[A[current]]: continue
    checked[A[current]] = True
    nexts.append(A[current])

  print(sum(checked))



import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()