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
        input = """0+0+2*0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3*1+1*2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3*1*4+0+2*0+5*2+9*8*6+1+3"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  print(sum("0" not in s for s in input().split("+")))
# resolve()

if __name__ == "__main__":
    unittest.main()
