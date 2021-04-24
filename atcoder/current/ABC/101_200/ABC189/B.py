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
        input = """2 15
200 5
350 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 10
200 5
350 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 1000000
1000 100
1000 100
1000 100"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  N, X = map(int, input().split(" "))
  t = 0
  X*=100
  for i in range(N):
    V, P = map(int, input().split(" "))
    t+=V*P
    if t > X:
      print(i+1)
      return

  print(-1)

resolve()

if __name__ == "__main__":
    unittest.main()
