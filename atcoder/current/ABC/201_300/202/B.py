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
        input = """0601889"""
        output = """6881090"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """86910"""
        output = """01698"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """01010"""
        output = """01010"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  dictionary = {
    "0":"0",
    "1":"1",
    "6":"9",
    "8":"8",
    "9":"6",
  }
  S = reversed([dictionary[x] for x in list(input())])

  print("".join(S))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
