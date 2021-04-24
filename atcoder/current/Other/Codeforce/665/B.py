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
2 3 2
3 3 1
4 0 1
2 3 0
0 0 1
0 0 1"""
        output = """4
2
0"""
        self.assertIO(input, output)


def resolve():
  loop_n = int(input())
  for _ in range(loop_n):
    A = [int(x) for x in input().split(" ")]
    B = [int(x) for x in input().split(" ")]
    ans = 0
    if A[2] >= B[1]:
      ans += 2 * B[1]
      A[2] -= B[1]
      B[1] = 0
    else:
      ans += 2 * A[2]
      A[2] = 0
      B[1] -= A[2]
    
    if B[2] >= A[0]:
      B[2] -= A[0]
      A[0] = 0
    else:
      A[0] -= B[2]
      B[2] = 0

    if B[2] >= A[2]:
      B[2] -= A[2]
      A[2] = 0
    else:
      A[2] -= B[2]
      B[2] = 0
    
    ans -= 2*B[2]

    print(ans)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
  unittest.main()