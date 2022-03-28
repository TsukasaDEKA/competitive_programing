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
        input = """4"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """109109109109109109"""
        output = """109109108641970782"""
        self.assertIO(input, output)

def resolve():
  from math import sqrt, ceil

  inf = 10**10+1
  # N+1 の丸太を切って、どれだけ徳ができるか？
  # 1+2+...+N の一般項は n*(n+1)/2
  N = int(input())
  gain = inf
  for i in reversed(range(ceil(sqrt(2*(N+1))))):
    if N+1 >= i*(i+1)//2:
      gain = i-1
      break
  print(N-gain)

resolve()

if __name__ == "__main__":
    unittest.main()
