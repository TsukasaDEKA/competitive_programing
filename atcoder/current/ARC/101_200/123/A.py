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
        input = """4 8 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 2 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1000000000000000 1 1000000000000000"""
        output = """999999999999999"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A = [int(x) for x in input().split(" ")]
  tar = 2*A[1]-A[0]
  if tar >= A[2]:
    print(tar-A[2])
    return

  ans = (A[2]-tar+1)//2
  tar += ((A[2]-tar+1)//2)*2
  ans += tar-A[2]
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()