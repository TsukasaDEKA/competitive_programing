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
        input = """10000"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000003"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9876543210"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  ans = len(str(N))

  for i in range(2, int(-(-N**0.5//1))+1):
    if N%i==0:
      ans = min(ans, len(str(max(i, N//i))))
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()

