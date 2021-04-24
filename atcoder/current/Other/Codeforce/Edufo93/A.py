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
7
4 6 11 11 15 18 20
4
10 10 10 11
3
1 1 1000000000"""
        output = """2 3 6
-1
1 2 3"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  for _ in range(N):
    length_of_array = int(input())
    A = [int(x) for x in input().split(" ")]
    isFound = False
    for i in range(length_of_array - 2):
      if A[i] + A[i+1] <= A[length_of_array-1]:
        isFound = True
        print(i+1, i+2, length_of_array)
        break
    if not isFound:
      print(-1)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()