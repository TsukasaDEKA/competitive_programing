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
        input = """CODEFESTIVAL"""
        output = """CODE"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """CODEFESTIVALFESTIVAL"""
        output = """CODEFESTIVAL"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """YAKINIKUFESTIVAL"""
        output = """YAKINIKU"""
        self.assertIO(input, output)

def resolve():
  print(input()[:-8])

# resolve()

if __name__ == "__main__":
    unittest.main()
