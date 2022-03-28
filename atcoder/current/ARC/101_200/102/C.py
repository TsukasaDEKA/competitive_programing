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
        input = """3 2"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31415 9265"""
        output = """27"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """35897 932"""
        output = """114191"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  # a, b, c がとりうる値の個数を求めて 3 乗すると答えが出る。
  ans = (N//K)**3
  # K が偶数の時は (1/2+S)*K の個数も含まれる。
  if not K%2: ans += ((N-K//2)//K+1)**3
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
