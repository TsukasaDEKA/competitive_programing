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

    def test_入力例１(self):
        input = """10 4
100
300
600
700
800
400
500
800
900
900"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例２(self):
        input = """10 3
10
40
50
80
90
30
20
40
90
95"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例３(self):
        input = """8 4
1
2
3
4
5
6
7
8"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例４(self):
        input = """8 2
100000
90000
50000
30000
10000
4000
200
1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 順に見ていって、前に見た数字よりも真に大きくなってたら連続した回数を記録する。
  N, K = map(int, input().split(" "))
  A = [int(input()) for _ in range(N)]

  ans = 0
  count = 1
  for i in range(1, N):
    if A[i-1] < A[i]: count+=1
    else:
      ans+= max(0, count - K + 1)
      count = 1
  ans+= max(0, count - K + 1)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
