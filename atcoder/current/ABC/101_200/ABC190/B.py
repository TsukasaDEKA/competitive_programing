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
        input = """4 9 9
5 5
15 5
5 15
15 15"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 691 273
691 997
593 273
691 273"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 100 100
10 11
12 67
192 79
154 197
142 158
20 25
17 108"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N, S, D = map(int, input().split(" "))

  for i in range(N):
    X, Y = map(int, input().split(" "))
    if X < S and Y > D:
      print("Yes")
      return
  print("No")

resolve()

if __name__ == "__main__":
    unittest.main()
