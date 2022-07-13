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
        input = """3"""
        output = """1
1 1
1 2 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10"""
        output = """1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  ans = [[1] for _ in range(N)]

  for i in range(1, N):
    for j in range(1, i+1):
      if i == j:
        ans[i].append(1)
      else:
        ans[i].append(ans[i-1][j-1] + ans[i-1][j])

  for a in ans:
    print(*a)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()