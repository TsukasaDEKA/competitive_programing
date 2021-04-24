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
        input = """7 1 3 6 7
.#..#.."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 1 3 7 6
.#..#.."""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """15 1 3 15 13
...#.#...#.#..."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 1 2 5 4
..#.."""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  # C < D の時、ふぬけ君を先に D まで移動させて、その後すぬけ君を C に移動させられるか判定すれば良い。
  # C > D の時が厄介で、どこかですぬけ君はふぬけ君を追い越さなきゃいけないので、
  # 3個以上の連続した . が B ~ C の間にあるか確認すれば良い。
  # A ~ D までのどこかに連続した # があると達成できない。
  # AB#CD みたいなパターンは No になる。
  N, A, B, C, D = [int(x)-1 for x in input().split(" ")]
  S = input()

  for i in range(A+1, max(C, D)):
    if S[i-1:i+1] == "##":
      print("No")
      return
  if C < D:
    print("Yes")
    return

  for i in range(B, D+1):
    if S[i-1:i+2] == "...":
      print("Yes")
      return
  print("No")
  
resolve()

if __name__ == "__main__":
    unittest.main()
