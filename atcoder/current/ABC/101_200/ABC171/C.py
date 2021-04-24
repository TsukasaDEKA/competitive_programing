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
        input = """26"""
        output = """z"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """703"""
        output = """aaa"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """123456789"""
        output = """jjddja"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """18278"""
        output = """zzz"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  N_to_str = ""
  alphabet_list = "zabcdefghijklmnopqrstuvwxyz"
  # N -= 1
  while N > 0:
    N-=1
    N_to_str=alphabet_list[N%26+1]+N_to_str
    # if N==26:
    #   break
    N = (N-N%26)//26
  print(N_to_str)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
