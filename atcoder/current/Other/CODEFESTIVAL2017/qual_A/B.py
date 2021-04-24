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
        input = """2 2 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 5 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7 9 20"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  # 行同士、列同士はそれぞれ独立しているので、並び替えても答えに影響を与えない。
  # そう考えると、それぞれ行のボタンと列のボタンを何個押すかについて探索すれば良くて、
  # その場合の黒の個数は、(押した行のボタンの個数*押してない列のボタンの個数) + (押してない行のボタンの個数*押した列のボタンの個数) になる。
  H, W, K = map(int, input().split(" "))
  for h in range(H+1):
    for w in range(W+1):
      if h*(W-w) + (H-h)*w == K:
        print("Yes")
        return
  print("No")

resolve()

if __name__ == "__main__":
    unittest.main()
