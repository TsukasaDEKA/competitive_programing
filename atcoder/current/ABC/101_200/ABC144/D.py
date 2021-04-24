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
        input = """2 2 4"""
        output = """45.0000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12 21 10"""
        output = """89.7834636934"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 1 8"""
        output = """4.2363947991"""
        self.assertIO(input, output)

def resolve():
  from math import degrees, atan
  # 傾ける軸と並行に水を切断すると、台形か直角三角形になる。
  # そこから体積を求めて、台形の底辺(か、三角形の一辺？) が b になる角度を求める。
  # 先に X/A をして水の断面積に変換してからの方が楽そう。
  A, B, X = map(int, input().split(" "))
  # 断面積
  cross = X/A
  if 2*cross > A*B:
    # 断面が台形の場合、
    Y = (2*cross)/A - B 
    print(degrees(atan( (B - Y) / A )))
    return
  # 断面が三角形の場合
  Y=(2*cross)/B
  print(degrees(atan( B / Y )))
resolve()

if __name__ == "__main__":
    unittest.main()
