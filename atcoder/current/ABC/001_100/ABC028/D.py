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
        input = """3 2"""
        output = """0.48148148148148148148"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 1"""
        output = """0.25925925925925925926"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """765 573"""
        output = """0.00147697396984624371"""
        self.assertIO(input, output)

def resolve():
  # N**3 パターンが存在する。
  # その内中央値が K であるものの個数を計算する。
  # 中央値なので、K は必ず一つ必要。
  # 残りの 2 個を選ぶときの組み合わせを考える。
  # K が 3 個の時、一通り
  # K が 2 個の時、K の選び方は 3 通り、残りの一つの選び方は K 以外の全て (N-1) 
  # K が 1 個の時、K の選び方は 3 通り。残りの二つの選び方は K 未満が一つと K を超えない物を一つ
  N, K = map(int, input().split(" "))
  ans = 1
  ans += 3*(N-1)
  ans += 3*2*(K-1)*(N-K)
  print(ans/(N**3))

resolve()

if __name__ == "__main__":
    unittest.main()
