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
        input = """2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """199999 200000"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """101 139"""
        output = """34"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A, B = map(int, input().split(" "))
  # X の倍数が 2 個とれればいい。X を全探索

  ans = 1
  for i in reversed(range(1, B)):
    x = i*((A+i-1)//i)
    if x <= B and x+i <= B:
      ans = i
      break

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
