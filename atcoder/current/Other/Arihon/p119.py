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
        input = """2
10
11"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
000
100
010"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1110
1100
1100
1000"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
10000001
10000000
10000000
10000000
10000000
10000010
10001000
10001000"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  grid = [0]*N
  for i in range(N):
    row = list(input())
    for j in reversed(range(N)):
      if row[j] == "1": break

    grid[i] = j

  ans = 0
  for i in range(N-1):
    if grid[i] <= i: continue

    j = i
    while grid[j] > i:
      j+=1
      if j >= N:
        print(-1)
        return
    # ここから入れ替え
    for k in reversed(range(i, j)):
      grid[k], grid[k+1] = grid[k+1], grid[k]
      ans+=1

  print(ans)
resolve()

if __name__ == "__main__":
  unittest.main()