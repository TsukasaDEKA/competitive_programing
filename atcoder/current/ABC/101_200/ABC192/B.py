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
        input = """dIfFiCuLt"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """eASY"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """a"""
        output = """Yes"""
        self.assertIO(input, output)

alpha2num = lambda c: ord(c) - ord('A')

def resolve():
  S = list(input())

  for i in range(len(S)):
    if i%2 and alpha2num(S[i]) >= 32:
      print("No")
      return
    if i%2==0 and alpha2num(S[i]) <= 25:
      print("No")
      return

  print("Yes")

resolve()

if __name__ == "__main__":
    unittest.main()

