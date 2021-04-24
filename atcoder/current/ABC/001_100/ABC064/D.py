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
        input = """3
())"""
        output = """(())"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
)))())"""
        output = """(((()))())"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
))))(((("""
        output = """(((())))(((())))"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  S = list(input())

  # "(" は左端に、")" は右端に入れることになるので、既にペアになってない "(" と ")" を数えれば良い。
  free_left_count = 0
  free_right_count = 0
  for s in S:
    if s=="(":
      free_left_count+=1
    else:
      if free_left_count:
        free_left_count-=1
      else:
        free_right_count+=1

  print("("*free_right_count + "".join(S) + ")"*free_left_count)

resolve()

if __name__ == "__main__":
    unittest.main()
