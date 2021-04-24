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
        input = """3 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """16 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """12 15"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
  inf = 10**10+1
  X, Y = map(int, input().split(" "))


  print("Yes" if min(X, Y) + 3 > max(X, Y) else "No")

resolve()

if __name__ == "__main__":
    unittest.main()
