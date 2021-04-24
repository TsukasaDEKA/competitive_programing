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
        input = """16"""
        output = """pon"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """2"""
        output = """hon"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """183"""
        output = """bon"""
        self.assertIO(input, output)

def resolve():
  N = input()
  if int(N[-1]) in [2,4,5,7,9]:
    print("hon")
    return True
  if int(N[-1]) in [0,1,6,8]:
    print("pon")
    return True
  print("bon")

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()