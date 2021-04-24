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
        input = """5
6
8
1
2
3"""
        output = """21"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
3
1
4
1
5
9"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
5
5
1"""
        output = """8"""
        self.assertIO(input, output)

from collections import deque

def resolve():
  N = int(input())
  A = sorted([int(input()) for _ in range(N)])
  A = deque(A)

  left = A.popleft()
  right = A.pop()
  ans = abs(left-right)

  while A:
    # deque の先頭と末尾、left と right をそれぞれ比較して、最大になる組み合わせで入れ替えをする。
    max_val = max(abs(A[0]-left), abs(A[0]-right), abs(A[-1]-left), abs(A[-1]-right))
    ans+=max_val
    if max_val == abs(A[0]-left):
      left=A.popleft()
      continue
    if max_val == abs(A[0]-right):
      right=A.popleft()
      continue
    if max_val == abs(A[-1]-left):
      left=A.pop()
      continue
    if max_val == abs(A[-1]-right):
      right=A.pop()
      continue
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
