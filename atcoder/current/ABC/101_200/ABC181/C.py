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

#     def test_Sample_Input_1(self):
#         input = """4
# 0 1
# 0 2
# 0 3
# 1 1"""
#         output = """Yes"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """14
5 5
0 1
2 5
8 0
2 1
0 0
3 6
8 6
5 9
7 9
3 4
9 2
9 8
7 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  inf = 10**9
  points = [[int(x) for x in input().split(" ")] for _ in range(N)]

  for i in range(N-1):
    tilts = set()
    for j in range(i+1,N):
      diff_x = points[i][0]-points[j][0]
      diff_y = points[i][1]-points[j][1]
      if diff_y == 0:
        tilt = inf
      else:
        tilt = diff_x/diff_y
      if tilt in tilts:
        print("Yes")
        return True
      tilts.add(tilt)
  print("No")

if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
