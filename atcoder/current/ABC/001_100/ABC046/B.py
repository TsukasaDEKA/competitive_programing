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
        input = """2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 10"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  # 端から順に塗っていくと考えると簡単に解ける。
  N, K = map(int, input().split(" "))
  ans = K*pow(K-1, N-1)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
