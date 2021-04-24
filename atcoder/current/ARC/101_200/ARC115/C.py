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
        input = """4"""
        output = """1 2 2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2"""
        output = """1 2"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  ans = [1]*(N+1)


  n = N
  for i in range(2, N+1):
    for t in range(i, N+1, i):
      ans[t]+=1

  print(*ans[1:])

resolve()

if __name__ == "__main__":
    unittest.main()
