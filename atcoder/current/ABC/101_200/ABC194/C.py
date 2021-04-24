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
2 8 4"""
        output = """56"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
-5 8 9 -4 -3"""
        output = """950"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  inte_A = [0]*(N+1)
  double_inte_A = [0]*(N+1)
  for i in range(N):
    inte_A[i+1] = inte_A[i] + A[i]
    double_inte_A[i+1] = double_inte_A[i] + A[i]*A[i]
  
  ans = 0
  for i in range(N-1):
    A_o = (N-1-i) * (double_inte_A[i+1]-double_inte_A[i])
    A_sub = double_inte_A[-1]-double_inte_A[i+1]
    dis = 2*A[i]*(inte_A[-1]-inte_A[i+1])

    ans += A_o + A_sub - dis
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
