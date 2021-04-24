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
        input = """4 2
1 2 -3 -4"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 3
-1 -2 -3 -4"""
        output = """1000000001"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 1
-1 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 10
1000000000 100000000 10000000 1000000 100000 10000 1000 100 10 1"""
        output = """999983200"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  abs_sorted_A = sorted(A, key=abs, reverse=True)

  if len([i for i in abs_sorted_A if i > 0]) == 0 and K%2==1:
    if 0 in abs_sorted_A:
      print(0)
      return True
    else:
      result = 1
      abs_sorted_A.reverse()
      for temp_abs_a in abs_sorted_A[:K]:
        result *= temp_abs_a
      print(result%10**9+7)
      return True

  temp_abs_A = abs_sorted_A[:K]
  # print(abs_sorted_A[:K])
  # print(abs_sorted_A[K:])
  result = 1
  if len([i for i in temp_abs_A if i < 0])%2 == 0:
    for temp_abs_a in temp_abs_A:
      result *= temp_abs_a
    print(result%(10**9+7))
    return True
  else:
    if len([i for i in abs_sorted_A[K:] if i < 0]) == 0:
      

  print(result%(10**9+7))

if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
