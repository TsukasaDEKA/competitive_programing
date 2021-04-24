
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

    def test_入力例_1(self):
        input = """5
3 3"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
3 3"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 2"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000000
1000000000 1"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9
3 5"""
        output = """Takahashi"""
        self.assertIO(input, output)

def resolve():
  # DP っぽい
  # A==B だったら相手の取れる個数 + 1 の倍数 にして、相手に渡せば勝ち確定
  # N = 3, A, B = 2, 2 の場合、後手必勝
  # N = 4, A, B = 2, 2 の場合、先手必勝
  # N = 5, A, B = 2, 2 の場合、先手必勝
  # N = 6, A, B = 2, 2 の場合、後手必勝
  # N = 6, A, B = 3, 3 の場合、後手必勝
  # A != B だったら多い方が勝ちそう (なんとなく)
  # N = 6, A, B = 2, 3 の場合、後手必勝

  N = int(input())
  A, B = map(int, input().split(" "))
  if A >= N:
    print("Takahashi")
    return

  if A == B:
    if N%(A+1) != 0:
      print("Takahashi")
      return
    print("Aoki")
    return
  
  print("Takahashi" if A > B else "Aoki")

resolve()

if __name__ == "__main__":
    unittest.main()

