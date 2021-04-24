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
        input = """3 2"""
        output = """10"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """200000 200001"""
        output = """1"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """141421 35623"""
        output = """220280457"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  N, K = map(int, input().split(" "))

  count = 0
  for i in range(K, N+1):
    minimum = int(i*(i-1)/2)
    maximum = int(i*(2*N-i+1)/2)
    count += maximum - minimum + 1
  count += 1
  print(count%mod)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()