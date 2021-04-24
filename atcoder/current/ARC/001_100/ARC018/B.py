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

    def test_入力例１(self):
        input = """3
1 1
1 2
3 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
1 1
1 2
2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3
1 1
2 2
3 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """8
3 1
4 1
5 9
2 6
5 3
5 8
9 7
9 3"""
        output = """38"""
        self.assertIO(input, output)


def resolve():
  # N<=100 なので総当たりしても大丈夫そう。
  N = int(input())
  X_Y = [list(map(int, input().split(" "))) for _ in range(N)]

  ans = 0
  for i in range(N-2):
    for j in range(i+1, N-1):
      for k in range(j+1, N):
        p0 = X_Y[i]
        p1 = X_Y[j]
        p2 = X_Y[k]
        area = abs((p1[0]-p0[0])*(p2[1]-p0[1]) - (p2[0]-p0[0])*(p1[1]-p0[1]))
        if area%2==0 and area != 0:
          # print(p0, p1, p2, area)
          ans+=1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
