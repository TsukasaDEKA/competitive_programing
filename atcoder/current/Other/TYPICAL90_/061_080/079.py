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
        input = """3 3
0 0 0
0 0 0
0 0 0
1 1 0
1 1 0
0 0 0"""
        output = """Yes
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 1 0
0 0 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5
6 17 18 29 22
39 50 25 39 25
34 34 8 25 17
28 48 25 47 42
27 47 24 32 28
4 6 3 29 28
48 50 21 48 29
44 44 19 47 28
4 49 46 29 28
4 49 45 1 1"""
        output = """Yes
140"""
        self.assertIO(input, output)

def resolve():
  # 左上から右下にかけて調整しながら B にマッチできるか確認していけば OK
  # 最後に縁をチェックする。
  H, W = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]
  B = [[int(x) for x in input().split(" ")] for _ in range(H)]

  count = 0
  for h in range(H-1):
    for w in range(W-1):
      diff = B[h][w] - A[h][w]
      for i in range(2):
        for j in range(2):
          A[h+i][w+j] += diff
      count+=abs(diff)

  for h in range(H):
    if A[h][W-1] != B[h][W-1]:
      print("No")
      return

  for w in range(W):
    if A[H-1][w] != B[H-1][w]:
      print("No")
      return

  print("Yes")
  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()