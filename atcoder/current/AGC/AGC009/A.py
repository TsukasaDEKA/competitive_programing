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
3 5
2 7
9 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
3 1
4 1
5 9
2 6
5 3
5 8
9 7"""
        output = """22"""
        self.assertIO(input, output)

def resolve():
  # N 個目のボタンから逆順に押していく。
  # (B-1) - (push_count + A + (B-1))%B 回押せば良い。
  N = int(input())
  A_B = [list(map(int, input().split(" "))) for _ in range(N)]
  push_count = 0
  for A, B in reversed(A_B):
    push_count+=(B-1) - (push_count + A + (B-1))%B
  print(push_count)

resolve()

if __name__ == "__main__":
    unittest.main()
