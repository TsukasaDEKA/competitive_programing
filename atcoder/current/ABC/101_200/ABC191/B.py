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
        input = """5 5
3 5 6 5 4"""
        output = """3 6 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
3 3 3"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  _, X = input().split(" ")
  print(*[x for x in input().split(" ") if x != X], sep=" ")

resolve()

if __name__ == "__main__":
    unittest.main()
