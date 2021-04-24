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
        input = """3
1 2 3
5 2 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 1 4 1 5
2 7 1 8 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
2 7 1 8 2
3 1 4 1 5"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]

  # それぞれ比較する。
  # Ai > Bi なら、手順を実行しなければいけない回数が上がる。
  # Ai < Bi なら、手順を実行できる回数が上がる。
  # 手順を実行できる回数 >= 手順を実行しなければいけない回数なら Yes、そうでないなら No
  times_of_to_do = 0
  times_of_can_do = 0
  for a, b in zip(A, B):
    if a >= b: times_of_to_do += a-b
    else: times_of_can_do += (b-a)//2
  print("Yes" if times_of_to_do <= times_of_can_do else "No")

resolve()


if __name__ == "__main__":
    unittest.main()
