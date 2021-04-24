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
-3 6
4 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
4 5
-1 -3"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1 3 5
3 -6 3"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())

  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  ans = 0
  for i in range(N):
    ans+=A[i]*B[i]
  
  print("Yes" if ans == 0 else "No")

resolve()


if __name__ == "__main__":
    unittest.main()
