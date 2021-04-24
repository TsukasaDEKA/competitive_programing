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
        input = """1988 2014"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """997 1003"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 2000000000"""
        output = """485000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 4 の倍数の年の数 - 100 の倍数の年 + 400 の倍数の年。
  # 境界値処理が厄介。+ 1 年とかで調整？
  A, B = map(int, input().split(" "))
  ans = (B//4-(A-1)//4) - (B//100-(A-1)//100) + (B//400-(A-1)//400)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
