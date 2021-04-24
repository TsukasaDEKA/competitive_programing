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
        input = """725"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1600"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  X = int(input())

  rank = 0
  if X<=599:
    print(8)
    return True

  if X<=799:
    print(7)
    return True  

  if X<=999:
    print(6)
    return True  

  if X<=1199:
    print(5)
    return True  

  if X<=1399:
    print(4)
    return True  

  if X<=1599:
    print(3)
    return True  

  if X<=1799:
    print(2)
    return True  

  if X<=1999:
    print(1)
    return True  

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
