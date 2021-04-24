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
        input = """3
Mozart plays magic."""
        output = """7003 756 791"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
Columbus found USA."""
        output = """15716 492 6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
I have a scissors for right hand."""
        output = """85 616606 40 0983 892"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
abc ab aa aiueo"""
        output = """11 1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """4
aaa aa a aa"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  _ = int(input())
  print(*(a for a in ("".join(str("zrbcdwtjfqlvsxpmhkng".find(c.lower())//2) for c in list(w) if c.lower() in "zrbcdwtjfqlvsxpmhkng") for w in input().split(" ")) if a), sep=" ")

# resolve()

if __name__ == "__main__":
    unittest.main()
