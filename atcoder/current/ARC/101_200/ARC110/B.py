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
        input = """4
1011"""
        output = """9999999999"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """22
1011011011011011011011"""
        output = """9999999993"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
110"""
        output = """9999999999"""
        self.assertIO(input, output)

from math import ceil

def resolve():
  N = int(input())
  T = input()

  if T=="0" or T=="10" or T=="11":
    print(10**10)
    return
  if T=="1":
    print(2*10**10)
    return
  
  sample = "110"*(ceil(N/3)+1)
  needs_num = 1
  for i in range(3):
    if sample[i:i+N] == T:
      print(10**10-ceil((N+i)/3)+1)
      return
  print(0)

resolve()

if __name__ == "__main__":
    unittest.main()
