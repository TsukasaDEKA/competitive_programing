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
        input = """2012/05/02"""
        output = """2013/01/01"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2020/05/02"""
        output = """2020/05/02"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2088/02/28"""
        output = """2088/02/29"""
        self.assertIO(input, output)

def resolve():
  # Y//(M*D) が割り切れれば良い。愚直にやっていく。
  from datetime import date, timedelta
  day = date(*[int(x) for x in input().split("/")])
  while day.year%(day.month*day.day):
    day+=timedelta(1)
  print(day.strftime("%Y/%m/%d"))
# resolve()

if __name__ == "__main__":
    unittest.main()
