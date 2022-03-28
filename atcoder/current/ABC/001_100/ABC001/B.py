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
        input = """15000"""
        output = """65"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """75000"""
        output = """89"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """200"""
        output = """02"""
        self.assertIO(input, output)

def resolve():
  M = int(input())
  vv = 0
  if M < 100:
    vv = 0
  elif M <= 5000:
    vv = (M*10)//1000
  elif M <= 30000:
    vv = M//1000+50
  elif M <= 70000:
    vv = (M//1000-30)//5+80
  else:
    vv = 89

  print('%02d'%vv)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()