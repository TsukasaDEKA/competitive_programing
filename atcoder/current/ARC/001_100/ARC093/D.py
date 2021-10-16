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
        input = """2 3"""
        output = """3 3
##.
..#
#.#"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 8"""
        output = """3 5
#.#.#
.#.#.
#.#.#"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1"""
        output = """4 2
..
#.
##
##"""
        self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """3 14"""
#         output = """8 18
# ..................
# ..................
# ....##.......####.
# ....#.#.....#.....
# ...#...#....#.....
# ..#.###.#...#.....
# .#.......#..#.....
# #.........#..####."""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """500 500"""
        output = """8 18
..................
..................
....##.......####.
....#.#.....#.....
...#...#....#.....
..#.###.#...#.....
.#.......#..#.....
#.........#..####."""
        self.assertIO(input, output)

def resolve():
  # 上半分を黒、下半分を白で塗り潰す。
  # 黒の領域に 1 マスずつ間を開けて白で塗りつぶしたマスを A-1 個置いていく。
  # 白の領域に 1 マスずつ間を開けて黒で塗りつぶしたマスを B-1 個置いていく。
  # A, B <= 500 なので、この解き方で十分な数の個数の連結成分を作ることができる。

  A, B = map(int, input().split(" "))
  ans = [["#"]*100 for _ in range(50)] + [["."]*100 for _ in range(50)]
  for i in range(A-1):
    ans[2*(i//50)][2*(i%50)] = "."

  for i in range(B-1):
    ans[2*(i//50)+51][2*(i%50)] = "#"

  print("100 100")
  for a in ans:
    print("".join(a))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()