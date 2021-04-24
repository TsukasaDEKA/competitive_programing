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
    def test_input_1(self):
        input = """117"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        input = """123"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        input = """777"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
    N = list(input())
    if ("7" in N):
      print("Yes")
    else:
      print("No")

if __name__ == "__main__":
    unittest.main()

