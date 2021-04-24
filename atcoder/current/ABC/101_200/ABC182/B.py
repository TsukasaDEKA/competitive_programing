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
3 12 7"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
8 9 18 90 72"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
1000 1000 1000 1000 1000"""
        output = """1000"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  ans = 2
  max_count = 0
  for k in range(2, 1001):
    temp_count = 0
    for a in A:
      if a%k==0: temp_count+=1
    if max_count <= temp_count:
      max_count = temp_count
      ans = k
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
