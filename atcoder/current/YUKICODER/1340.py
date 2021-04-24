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
        input = """5 6 10
0 1
1 2
2 3
3 0
1 4
4 0"""
        output = """30"""
        self.assertIO(input, output)


import sys
sys.setrecursionlimit(500*500)

def resolve():
  # T が 10**18 なのでシミュレートは無理。
  # ループ があるか無いかで話が変わりそう。
  # ノード N について、

  N, M, T = map(int, input().split(" "))
  ROUTE = [set()]*N
  for _ in range(M):
    A, B = map(int, input().split(" "))
    ROUTE[A].add(B)
  print(N)

# resolve()

if __name__ == "__main__":
  unittest.main()