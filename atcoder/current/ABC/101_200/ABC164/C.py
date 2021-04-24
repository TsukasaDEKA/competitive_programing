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
        input = """3
apple
orange
apple"""
        output = """2"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """5
grape
grape
grape
grape
grape"""
        output = """1"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """4
aaaa
a
aaa
aa"""
        output = """4"""
        self.assertIO(input, output)

from collections import Counter

def resolve():
  N = int(input())
  S = []
  for i in range(N):
    S.append(input())

  c = Counter(S)
  
  print(len(c))


if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()