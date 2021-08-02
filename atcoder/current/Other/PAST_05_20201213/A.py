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
        input = """xooox"""
        output = """o"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """xxxxx"""
        output = """x"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """xoxxo"""
        output = """draw"""
        self.assertIO(input, output)

def resolve():
  S = list(input())

  current = ""
  count=0
  for s in S:
    if current == s: count+=1
    else:
      count = 1
      current = s
    if count == 3:
      print(current)
      return
  print("draw")

resolve()

if __name__ == "__main__":
    unittest.main()
