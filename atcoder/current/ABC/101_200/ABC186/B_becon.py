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
        input = """2 3
2 2 3
3 2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
99 99 99
99 0 99
99 99 99"""
        output = """792"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 2
4 4
4 4
4 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 1
4"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  h, w = map(int, input().split(" "))
  A = [list(map(int, input().split())) for i in range(h)]
  
  print(A)
  #print(min(min(A)))
  cun = 0
  
  for i in range(h):
    for j in range(w):
      if A[i][j] > min(min(A)):
        cun = cun + (A[i][j] - min(min(A)))
  
  print(cun)

# resolve()
if __name__ == "__main__":
    unittest.main()
