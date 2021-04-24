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
        input = """2 2 1 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 4 1"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4 8 0"""
        output = """36"""
        self.assertIO(input, output)

def resolve():
  ans = [0]
  H, W, A, B = map(int, input().split())
  coord = [0]*H*W
  from copy import copy

  def rec_func(arr, i, a, b):
    if sum(arr) == H*W:
      ans[0] += 1
      return

    if arr[i] == 1:
      rec_func(arr, i+1, a, b)
    else:
      if b:
        temp_arr = copy(arr)
        temp_arr[i] += 1
        rec_func(temp_arr, i+1, a, b-1)

      if a:
        if i%W != W-1:
          if arr[i+1] == 0:
            temp_arr = copy(arr)
            temp_arr[i] = temp_arr[i+1] = 1
            rec_func(temp_arr, i+1, a-1, b)

        if i+W < H*W:
          if arr[i+W] == 0:
            temp_arr = copy(arr)
            temp_arr[i] = temp_arr[i+W] = 1
            rec_func(temp_arr, i+1, a-1, b)

  rec_func(coord, 0, A, B)
  print(ans[0])

resolve()

if __name__ == "__main__":
    unittest.main()
