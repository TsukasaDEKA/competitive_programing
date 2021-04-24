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
8 5
4 4
7 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
11 7
3 2
6 7"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A_B = [list(map(int, input().split(" "))) for _ in range(N)]

  ans = inf
  for a in range(N):
    for b in range(N):
      temp = max(A_B[a][0], A_B[b][1]) if a!=b else A_B[a][0] + A_B[b][1]
      ans = min(ans, temp)

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
