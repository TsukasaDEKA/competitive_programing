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
        input = """6"""
        output = """3
1 2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12"""
        output = """6
2 5 1 2 5 1"""
        self.assertIO(input, output)

def resolve():
  W = int(input())

  ans = []
  for i in range(1, 100):
    ans.append(i)
    ans.append(i*100)
    ans.append(i*10000)
  
  ans.append(10**6)
  print(len(ans))
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()