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
        input = """4
WWRR"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
RR"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
WRWWRWRR"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  C = [0 if x == "W" else 1 for x in list(input())]
  red_seacher_index = N - 1
  white_seacher_index = 0

  counter = 0
  while white_seacher_index <= red_seacher_index:
    if C[white_seacher_index] == 0:
      # 赤を Tail 側から探して見つけたら入れ替える
      while white_seacher_index <= red_seacher_index:
        if C[red_seacher_index] == 1:
          C[white_seacher_index] = 1
          C[red_seacher_index] = 0
          counter += 1
          break
        red_seacher_index -= 1
    white_seacher_index += 1
  print(counter)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
