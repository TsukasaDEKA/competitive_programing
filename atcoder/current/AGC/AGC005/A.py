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
        input = """TSTTSS"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """SSTTST"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """TSSTTTSS"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  X = input()

  temp = ""
  for x in X:
    temp += x
    if temp[-2:] == "ST": temp = temp[:-2]
  print(len(temp))

resolve()

if __name__ == "__main__":
    unittest.main()
