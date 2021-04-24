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
        input = """erasedream"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """dreameraser"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """dreamerer"""
        output = """NO"""
        self.assertIO(input, output)


def resolve():
  S = input()
  candidates = ["dream", "dreamer", "erase", "eraser"]

  i = len(S)-1
  while i > 0:
    is_match = False
    for candidate in candidates:
      # print(S[i-len(candidate):i+1], candidate)
      if S[i-len(candidate)+1:i+1] == candidate:
        is_match = True
        i -= len(candidate)
        break
    
    # 一つもマッチしなかったら 終了
    if not is_match:
      print("NO")
      return

  print("YES")

resolve()

if __name__ == "__main__":
    unittest.main()
