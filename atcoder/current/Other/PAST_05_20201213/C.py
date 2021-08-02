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
        input = """123"""
        output = """3F"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2304"""
        output = """1S0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """35"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  num2alpha = lambda c: chr(c+64-9)
  N = int(input())

  if N==0:
    print(0)
    return

  ans = ""
  while N > 0:
    temp = N%36
    if temp > 9:
      ans = num2alpha(temp) + ans
    else:
      ans = str(temp) + ans
    N//=36
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
