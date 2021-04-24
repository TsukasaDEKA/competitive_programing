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
        input = """2 3
..#
#.."""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
.#
#."""
        output = """0"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """4 4
# ...#
# #...
# #...
# #..."""
#         output = """0"""
#         self.assertIO(input, output)

def resolve():
  H, W = map(int, input().split(" "))
  room_map = [list(input()) for x in range(H)]
  count = 0
  for w in range(W):
    for h in range(H):
      if room_map[h][w]==".":
        if w < W - 1:
          if room_map[h][w+1]==".": count += 1
        if h < H - 1:
          if room_map[h+1][w]==".": count += 1
  print(count)


if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
