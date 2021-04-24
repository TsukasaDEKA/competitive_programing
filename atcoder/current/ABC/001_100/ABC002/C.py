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
        input = """1 0 3 0 2 5"""
        output = """5.0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-1 -2 3 4 5 6"""
        output = """2.0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """298 520 903 520 4 663"""
        output = """43257.5"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  X_Y = [int(x) for x in input().split(" ")]
  for i in range(2, -1, -1):
    X_Y[i*2] -= X_Y[0]
    X_Y[i*2+1] -= X_Y[1]
  ans = abs(X_Y[2]*X_Y[5]- X_Y[3]*X_Y[4])/2
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
