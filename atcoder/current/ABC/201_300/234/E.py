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
        input = """152"""
        output = """159"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """88"""
        output = """88"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8989898989"""
        output = """9876543210"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """9"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect_left

  X = input()
  V = int(X)
  S = [int(x) for x in list(X)]
  N = len(S)

  if V <= 9:
    print(V)
    return
  table = set()

  # diff は -9 ~ 8 まで
  for diff in range(-9, 9):
    # print("diff", diff, file=sys.stderr)
    for start in range(10):
      current = start
      val = current
      for digit in range(1, N+4):
        if current+diff >= 10 or current+diff <= 0: break
        current = current+diff
        val = val+(current)*pow(10, digit)
        if val < V: continue
        if val in table: continue
        # print(val, file=sys.stderr)

        table.add(val)
  
  # print(table)
  table = sorted(list(table))
  # print(table)
  print(table[0])
  
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()