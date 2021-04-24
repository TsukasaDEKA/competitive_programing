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
        input = """3 10"""
        output = """0.145833333333"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100000 5"""
        output = """0.999973749998"""
        self.assertIO(input, output)

def resolve():
  # コインの裏だったらそこでゲームセット。
  # 最初のサイコロの目によって、連続で出さなきゃいけない表の数が決まる。
  # 連続で表がでる確率は O(p) (p < 18)で求まる。
  N, K = map(int, input().split(" "))
  ans = 0
  for i in range(1, N+1):
    count = 0
    while i < K:
      i*=2
      count+=1
    ans+=pow(0.5, count)

  print(ans/N)

resolve()

if __name__ == "__main__":
    unittest.main()
