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
3 1 2
4 2 2
331895368 154715807 13941326"""
        output = """20
32
409369707"""
        self.assertIO(input, output)
#     def test_Sample_Input_1(self):
#         input = """2
# 3 1 2
# 4 2 2"""
#         output = """20
# 32"""
#         self.assertIO(input, output)

def resolve():
  T = int(input())
  mod_base = 10**9+7
  for _ in range(T):
    N, A, B = map(int, input().split(" "))
    all_pattern = (N-A+1)**2 * (N-B+1)**2
    if all_pattern > mod_base:
      all_pattern %= mod_base
    X4 = (N-A-B+2)*(N-A-B+1)/2
    # if X4 > mod_base:
    #   X4 %= mod_base

    X3 = 2*int(X4)
    # if X3 > mod_base:
    #   X3 %= mod_base

    X2 = (N-A+1)*(N-B+1) - X3
    # if X2 > mod_base:
    #   X2 %= mod_base
    # negative_pattern = (K**2*A + K**2*(K-1)*A + int(K*(K+1)/2)**2)*4 + (N-3*(A-1))**2 * (A+B-1)**2
    X1 = X2**2
    if X1 > mod_base:
      X1 %= mod_base

    print((all_pattern-X1)%mod_base)



if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
