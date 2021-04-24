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
0224"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
123123"""
        output = """17"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """19
3141592653589793238"""
        output = """329"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = [int(x) for x in list(input())]
  ans = 0
  for target in range(1000):
    pin = [int(x) for x in list(str(target).zfill(3))]
    i=0
    for s in S:
      if s == pin[i]: i+=1
      if i >= 3:
        ans+=1
        break
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
