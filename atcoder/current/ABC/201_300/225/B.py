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
        input = """5
1 4
2 4
3 4
4 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
2 4
1 4
2 3"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
9 10
3 10
4 10
8 10
1 10
2 10
7 10
6 10
5 10"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  EDGES = [[] for _ in range(N)]
  for i in range(N-1):
    a, b = [int(x)-1 for x in input().split(" ")]
    EDGES[a].append(b)
    EDGES[b].append(a)
  for i in range(N):
    if len(EDGES[i]) == N-1:
      print("Yes")
      return
  print("No")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()