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
        input = """5
1 2 3 2 1"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6
3 3 4 1 2 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """6
1 5 2 3 4 2"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  # `D - Xor Sum 2` を簡単にした感じ。
  # 尺取で解けそう。
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  l = r = 0
  ans = 0
  while l < N and r < N:
    while l==r or A[r-1] < A[r]:
      r+=1
      if r >= N: break
    length = r - l
    ans += (length*(length+1))//2
    l = r
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
