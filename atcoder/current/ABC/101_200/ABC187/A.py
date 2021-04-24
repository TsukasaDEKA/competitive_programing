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
        input = """123 234"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """593 953"""
        output = """17"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 999"""
        output = """27"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  A, B = map(int, input().split(" "))
  ansA = 0
  for a in list(str(A)):
    ansA+=int(a)
  ansB = 0
  for b in list(str(B)):
    ansB+=int(b)
  print(max(ansA, ansB))

resolve()

if __name__ == "__main__":
    unittest.main()
