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
        input = """7 2 5
3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 4 2
3"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  A, B, C = map(int, input().split(" "))
  K = int(input())

  for _ in range(K):
    if A >= B:
      B *= 2
    elif B >= C:
      C *= 2
    
    if A < B and B < C:
      print("Yes")
      return True
  print("No")

if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
