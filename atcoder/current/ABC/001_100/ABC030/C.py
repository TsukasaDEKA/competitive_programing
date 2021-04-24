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

    def test_入力例1(self):
        input = """3 4
2 3
1 5 7
3 8 12 13"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1
1 1
1
1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6 7
5 3
1 7 12 19 20 26
4 9 15 23 24 31 33"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # インデックスと時間を管理しつつ何往復できるか数えていく
  N, M = map(int, input().split(" "))
  A_t, B_t = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]

  a_i = 0
  b_i = 0
  current_time = 0
  ans = 0
  while True:
    while A[a_i] < current_time:
      a_i += 1
      if a_i >= N:
        print(ans)
        return
    current_time = A[a_i] + A_t

    while B[b_i] < current_time:
      b_i += 1
      if b_i >= M:
        print(ans)
        return
    current_time = B[b_i] + B_t
    ans+=1

resolve()

if __name__ == "__main__":
    unittest.main()
