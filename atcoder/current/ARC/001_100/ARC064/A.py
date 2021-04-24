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
        input = """3 3
2 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 1
1 6 1 2 0 4"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 9
3 1 4 1 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2 0
5 5"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 部分和の更新なのでセグ木？
  # ai <=10**9 なのでシミュレートしていくと時間が足りない。
  # 2 <= i <= N の範囲で ai を見ていって、A[i-1] + A[i] が X 以下になる様に A[i] を減らしていく。
  # A[i] だけで足りなかったら A[i-1] も減らす。
  # 減らしたキャンディの総和をとる。O(N)
  N, X = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  ans = 0
  for i in range(1, N):
    diff = A[i-1] + A[i] - X
    if diff > 0:
      ans+=diff
      if A[i] >= diff:
        A[i]-=diff
      else:
        A[i-1] = diff-A[i]
        A[i]=0

  print(ans)

resolve()


if __name__ == "__main__":
    unittest.main()
