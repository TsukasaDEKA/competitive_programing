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
        input = """5
1 4 3 5 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """9
1 2 4 9 5 8 7 3 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """5
1 2 3 4 5"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  P = [int(x)-1 for x in input().split(" ")]

  ans = 0
  i = 0
  for i in range(N-1):
    if P[i] == i:
      if P[i+1] == i+1:
        P[i], P[i+1] = P[i+1], P[i]
      ans+=1   
  if P[N-1]==N-1: ans+=1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
