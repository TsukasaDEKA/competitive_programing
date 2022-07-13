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
        input = """3 50
30 20 10"""
        output = """Possible
2
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 21
10 10"""
        output = """Impossible"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 50
10 20 30 40 50"""
        output = """Possible
1
2
3
4"""
        self.assertIO(input, output)

def resolve():
  # a_i + a_i+1 となる i が L 以上になる
  inf = 10**18+1
  N, L = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  for i in range(N-1):
    if A[i] + A[i+1] >= L:
      print("Possible")
      for j in range(i):
        print(j+1)
      for j in range(N-1, i, -1):
        print(j)
      return
  else:
    print("Impossible")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()