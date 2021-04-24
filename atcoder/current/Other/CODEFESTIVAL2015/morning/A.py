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
        input = """5 3 100 60
86
23
49
39"""
        output = """45"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 3 100 60
92
100
95
99"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5 3 100 60
18
42
29
31"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """13 10 1000000000 645245296
492014535
611893452
729291030
392019922
293849201
474839528
702912832
341845861
102495671
908590572
812912432
129855439"""
        output = """986132796"""
        self.assertIO(input, output)

def resolve():
  N, K, M, R = map(int, input().split(" "))
  S = sorted([int(input()) for _ in range(N-1)], reverse=True)
  S.append(0)
  boarder = R*K
  current = sum(S[:K])
  if current >= boarder:
    print(0)
    return

  new_ = boarder - (current - S[K-1])
  if new_ <= M:
    print(new_)
    return
  print(-1)
# resolve()

if __name__ == "__main__":
    unittest.main()
