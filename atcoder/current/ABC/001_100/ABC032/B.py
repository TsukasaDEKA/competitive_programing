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
        input = """abcabc
2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """aaaaa
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """hello
10"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # S が短いので全パターン set に投げ込めば良さそう。
  S = input()
  K = int(input())
  ans = set()
  for i in range(len(S) - K + 1):
    ans.add(S[i:i+K])
  print(len(ans))

resolve()

if __name__ == "__main__":
    unittest.main()
