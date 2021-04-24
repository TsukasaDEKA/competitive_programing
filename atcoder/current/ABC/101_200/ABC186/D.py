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
5 1 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
31 41 59 26 53"""
        output = """176"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  A.sort()

  integra_A = [0]*(N+1)
  for i in range(N):
    integra_A[i+1] = integra_A[i]+A[i]
  
  ans = 0
  for i in range(1, N):
    ans+=A[i]*i - integra_A[i]
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
