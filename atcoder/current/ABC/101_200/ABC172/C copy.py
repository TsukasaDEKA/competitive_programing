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
        input = """3 4 240
60 90 120
80 150 80 150"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 4 730
60 90 120
80 150 80 150"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 4 1
1000000000 1000000000 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 3 10
10000
1 1 1"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
  N, M, K = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  a, b = [0], [0]
  for i in range(N):
    a.append(a[i] + A[i])
  for i in range(M):
    b.append(b[i] + B[i])

  print(a)
  ans, j = 0, M
  for i in range(N + 1):
    if a[i] > K:
      break
    while b[j] > K - a[i]:
      j -= 1
    ans = max(ans, i + j)
  print(ans)


# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
