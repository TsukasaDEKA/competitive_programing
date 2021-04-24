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
        input = """6 5
4 7 10 6 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 5
4 7 10 6 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 0"""
        output = """100"""
        self.assertIO(input, output)

def resolve():
  X, N = map(int, input().split(" "))
  if N == 0:
    print(X)
    return True

  p = [int(x) for x in input().split(" ")]
  set_p = set(p)

  for i in range(N+100):
    if (X-i) not in set_p:
      print(X-i)
      return True

    if (X+i) not in set_p:
      print(X+i)
      return True

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
