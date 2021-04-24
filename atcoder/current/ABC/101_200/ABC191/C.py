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
        input = """5 5
.....
.###.
.###.
.###.
....."""
        output = """4"""
        self.assertIO(input, output)


def resolve():
  n_x_y = [
    [(-1, 0), (-1, -1), (0, -1)],
    [(0, -1), ( 1, -1), (1,  0)],
    [(1,  0), ( 1,  1), (0,  1)],
    [(0,  1), (-1,  1), (-1, 0)],
  ]

  # 角の数を調べる。
  H, W = map(int, input().split(" "))
  S = [[x == "#" for x in list(input())] for _ in range(H)]

  count = 0
  for h in range(1, H-1):
    for w in range(1, W-1):
      if S[h][w]:
        for x_y in n_x_y:
          if not S[h+x_y[1][0]][w+x_y[1][1]] and not (S[h+x_y[0][0]][w+x_y[0][1]] ^ S[h+x_y[2][0]][w+x_y[2][1]]):
            count+=1

  print(count)

resolve()

if __name__ == "__main__":
    unittest.main()
