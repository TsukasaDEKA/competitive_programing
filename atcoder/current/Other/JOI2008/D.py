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
8 5
6 4
4 3
7 10
0 10
10
10 5
2 7
9 7
8 10
10 2
1 2
8 1
6 7
6 0
0 9"""
        output = """2 -3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
904207 809784
845370 244806
499091 59863
638406 182509
435076 362268
10
757559 866424
114810 239537
519926 989458
461089 424480
674361 448440
81851 150384
459107 795405
299682 6700
254125 362183
50795 541942"""
        output = """-384281 179674"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  M = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(M)]

  N = int(input())
  B = [[int(x) for x in input().split(" ")] for _ in range(N)]
  set_B = set([(x, y) for x, y in B])

  x, y = A[0]
  for i in range(N):
    x_, y_ = B[i]
    diff_x, diff_y = x_-x, y_-y

    for x__, y__ in A:
      x__ += diff_x
      y__ += diff_y
      if (x__, y__) not in set_B:
        break
    else:
      print(diff_x, diff_y, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()