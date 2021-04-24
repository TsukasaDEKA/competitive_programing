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
        input = """4 4 2 2
##..
...#
#.#.
.#.#"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5 1 4
#....
#####
....#"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5 4 2
.#..#
#.###
##...
#..#.
#.###"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  H, W, X, Y = map(int, input().split(" "))
  S = [list(input()) for _ in range(H)]
  X -= 1
  Y -= 1
  count = 1
  h = X
  w = Y
  while S[h][w] == ".":
    count+=1
    h+=1
    if h >= H:
      break

  h = X
  w = Y
  while S[h][w] == ".":
    count+=1
    h-=1
    if h < 0:
      break

  h = X
  w = Y
  while S[h][w] == ".":
    count+=1
    w-=1
    if w < 0:
      break

  h = X
  w = Y
  while S[h][w] == ".":
    count+=1
    w+=1
    if w >= W:
      break
  print(count-4)

resolve()

if __name__ == "__main__":
    unittest.main()
