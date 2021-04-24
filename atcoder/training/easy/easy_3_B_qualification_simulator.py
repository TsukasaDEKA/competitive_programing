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
        input = """10 2 3
abccabaabb"""
        output = """Yes
Yes
No
No
Yes
Yes
Yes
No
No
No"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12 5 2
cabbabaacaba"""
        output = """No
Yes
Yes
Yes
Yes
No
Yes
Yes
No
Yes
No
No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 2 2
ccccc"""
        output = """No
No
No
No
No"""
        self.assertIO(input, output)

def resolve():
  N, A, B= map(int, input().split(" "))
  S = list(input())

  sum_of_successful_candidate = 0
  sum_of_successful_b = 0

  for i, s in enumerate(S):
    if sum_of_successful_candidate >= A + B:
      for _ in range(N-i):
        print("No")
      return True

    if s == "a":
      sum_of_successful_candidate += 1
      print("Yes")
    elif s == "b" and sum_of_successful_b < B:
      sum_of_successful_candidate += 1
      sum_of_successful_b += 1
      print("Yes")
    else:
      print("No")

  return True


if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
