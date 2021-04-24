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
        input = """1010"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """27182818284590"""
        output = """107730272137364"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  if N < 10**3:
    print(0)
    return
  
  ans = 0
  for i in range(2, 10):
    if N < 10**(3*i):
      ans += (i-1)*(N-10**(3*(i-1))+1)
      print(ans)
      return
    else:
      ans += (i-1)*(10**(3*i)-10**(3*(i-1)))
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
