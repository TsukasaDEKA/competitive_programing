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
        input = """2
3
10 4 9
3
10 8 12"""
        output = """Case #1: PEEEEL
Case #2: AAAAAAAAAA
Case #3: CCODDEEJAAMDAAY"""
        self.assertIO(input, output)

def resolve():
  T = int(input())

  for t in range(1, T+1):
    N = int(input())
    request = list(range(1, N+1))
    print(*request)
    response = [int(x) for x in input().split(" ")]

    A = sorted(request+response, reverse=True)
    goal = sum(A)//2
    ans = []
    for i in range(2*N):
      if A[i] <= goal:
        ans.append(A[i])
        goal -= A[i]
    print(*ans, sep=" ")

resolve()

if __name__ == "__main__":
  unittest.main()