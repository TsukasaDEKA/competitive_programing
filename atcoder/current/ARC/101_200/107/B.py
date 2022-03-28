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
        input = """2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 1"""
        output = """16"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2525 -425"""
        output = """10314607400"""
        self.assertIO(input, output)

def calc_pattarn(N, K):
  return max(0, min(K-1, 2*N+1-K))

def resolve():
  N, K = map(int, input().split(" "))

  ans = 0
  for add_a_b in range(2, 2*N+1): ans += calc_pattarn(N, add_a_b)*calc_pattarn(N, add_a_b-K)
  print(ans)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
