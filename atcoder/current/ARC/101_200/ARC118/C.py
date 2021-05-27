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

    def test_入力例_1(self):
        input = """4"""
        output = """84 60 105 70"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  table = []
  for i in range(2, 10001, 2):
    count = 0
    if i%2 == 0 and (i%3 == 0 or i%5 == 0 or i%7 == 0):
      table.append(i)
      continue
    
  ans = table[:N-1]+[1155]
  print(*ans, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
