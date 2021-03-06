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
        input = """abcdZONefghi"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """ZONeZONeZONe"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """helloAtZoner"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = input()
  zone = "ZONe"
  count = 0
  for i in range(len(S)-3):
    if S[i:i+4] == zone:
      count+=1
  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
