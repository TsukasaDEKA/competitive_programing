import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """9 45000"""
        output = """4 0 5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20 196000"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000 1234000"""
        output = """14 27 959"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2000 20000000"""
        output = """2000 0 0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, Y = map(int, input().split(" "))
  for i in range(N+1):
    for j in range(N-i+1):
      k = N-i-j
      val = 10000*i+5000*j+1000*k
      if val == Y:
        print(i, j, k)
        return
  print(-1, -1, -1)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()