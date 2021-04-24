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

    # def test_Sample_Input_1(self):
    #     input = """0.2 0.8 1.1"""
    #     output = """3"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """0 0 2"""
    #     output = """13"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """42782.4720 31949.0192 99999.99"""
    #     output = """31415920098"""
    #     self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """0 0.2 0.13"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # R <= 10**5 なので、R**2 の点全てを求めようとすると厳しそう。
  # 縦に輪切りする。
  # X-R ~ X+R の範囲で探索する。 縦の格子点の個数を求める。
  # (x-a)**2 +(y-b)**2 = R**2
  from math import floor, ceil, isqrt
 
  base = 10**4
  inputs = input()
  X0, Y0, R0 = map(lambda a: int(a.replace('.', '')) * 10**(5-(len(a)-(a.find('.') % len(a)))), inputs.split(" "))
  X1, Y1, R1 = [int(float(x)*base) for x in inputs.split(" ")]
  X2, Y2, R2 = map(lambda a: 10**(5-(len(a)-(a.find('.') % len(a)))), inputs.split(" "))
  print(X0)
  print(X0 == X1 and Y0==Y1 and R0==R1)

# resolve()

if __name__ == "__main__":
    unittest.main()
