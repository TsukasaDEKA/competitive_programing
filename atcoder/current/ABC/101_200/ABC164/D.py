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
        input = """1817181712114"""
        output = """3"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """14282668646"""
        output = """2"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)
    def test_Sample_Input_4(self):
        input = """21"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # S の長さが 2*10**5 なので、愚直にやると厳しそう。
  # 倍数判定が O(1) でも組み合わせが 2*10**10 程度あるので厳しい。
  S = list(input())

  # print(count)
  print(S)
# resolve()

if __name__ == "__main__":
    unittest.main()