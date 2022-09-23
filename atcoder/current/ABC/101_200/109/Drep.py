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
        input = """2 3
1 2 3
0 1 1"""
        output = """3
2 2 2 3
1 1 1 2
1 3 1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
1 0
2 1
1 0"""
        output = """3
1 1 1 2
1 2 2 2
3 1 3 2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 5
9 9 9 9 9"""
        output = """2
1 1 1 2
1 3 1 4"""
        self.assertIO(input, output)

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]

def resolve():
  # 奇数だったら右に寄せて、最後右端だけ下に寄せる。
  H, W = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]

  ans = []
  for h in range(H-1):
    for w in range(W):
      if A[h][w]%2:
        A[h+1][w]+=1
        A[h][w]-=1
        ans.append((h+1, w+1, h+2, w+1))

  for w in range(W-1):
    if A[H-1][w]%2:
      A[H-1][w+1] += 1
      A[H-1][w] -= 1
      ans.append((H, w+1, H, w+2))

  print(len(ans))
  for a in ans:
    print(*a, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()