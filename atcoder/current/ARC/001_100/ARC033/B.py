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

    def test_入力例1(self):
        input = """3 2
1 3 5
1 2"""
        output = """0.2500000000"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """9 10
11 2 33 4 55 6 77 8 99
10 11 14 19 55 1000000000 4 5 7 8"""
        output = """0.2666666667"""
        self.assertIO(input, output)

def resolve():
  # 特に工夫しなくてもできそう。
  NA, NB = map(int, input().split(" "))
  A = set([int(x) for x in input().split(" ")])
  B = set([int(x) for x in input().split(" ")])

  AUB = A | B
  ANB = A & B
  print(len(ANB)/len(AUB))

resolve()

if __name__ == "__main__":
    unittest.main()
