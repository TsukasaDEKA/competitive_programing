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
        input = """10 2 20
9 11
13 17"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 2 20
9 11
13 16"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """15 3 30
5 8
15 17
24 27"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """20 1 30
20 29"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """20 1 30
1 10"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  N, M, T = map(int, input().split(" "))
  temp_N = N
  now = 0
  for i in range(M):
    A, B = map(int, input().split(" "))
    N-=(A-now)
    if N<=0:
      print("No")
      return
    N =min(N+(B-A), temp_N)
    now = B

  N-=(T-now)
  if N<=0:
    print("No")
    return
  print("Yes")

# resolve()

if __name__ == "__main__":
    unittest.main()
