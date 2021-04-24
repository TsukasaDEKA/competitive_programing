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
        input = """5 3
96 98 95 100 20"""
        output = """Yes
No"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
1001 869120 1001"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """15 7
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9"""
        output = """Yes
Yes
No
Yes
Yes
No
Yes
Yes"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  
  for i in range(K, N):
    if A[i-K] < A[i]:
      print("Yes")
    else:
      print("No")

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
