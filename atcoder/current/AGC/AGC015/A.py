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
        input = """4 4 6"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 7 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 3 3"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 最大と最小の 2 個は固定
  # A*(N-1)+Bが最小値で, B*(N-1)+A が最大値になる。
  # 累計は A*(N-1)+B ~ B*(N-1)+A の間で任意に変化させることができる。
  N, A, B = map(int, input().split(" "))
  print(max(0, (B-A)*(N-2) + 1))

resolve()

if __name__ == "__main__":
    unittest.main()
