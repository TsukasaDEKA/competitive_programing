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
        input = """2 2
3
2 1 1"""
        output = """1 1
2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5
5
1 2 3 4 5"""
        output = """1 4 4 4 3
2 5 4 5 3
2 5 5 5 3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1
1
1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  H, W = map(int, input().split(" "))
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  # 蛇腹状に塗っていく
  i = 0
  is_forward = True
  for _ in range(H):
    ans = [""] * W

    indexes = range(0, W) if is_forward else reversed(range(0, W))
    for w in indexes:
      ans[w] = str(i+1)
      A[i] -= 1
      if A[i] <= 0: i+=1
    print(" ".join(ans))
    is_forward = not is_forward

resolve()

if __name__ == "__main__":
    unittest.main()
