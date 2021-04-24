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
        input = """BBW"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """BWBWBW"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  # 似た問題解いたことある。
  S = list(input())

  ans=0
  black_count=0
  for s in S:
    if s=="B":black_count+=1
    else: ans+=black_count
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
