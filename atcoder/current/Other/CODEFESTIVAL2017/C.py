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
        input = """xabxa"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """ab"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """a"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """oxxx"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  
  # 前後から探索していって、探索する点が重なるかすれ違ったら終了
  ans = 0
  i = 0
  r_i = len(S)-1
  while i < r_i:
    if S[i]==S[r_i]:
      i += 1
      r_i-=1
      continue
    if S[i]=="x":
      i+=1
      ans+=1
      continue
    if S[r_i]=="x":
      r_i-=1
      ans+=1
      continue
    print(-1)
    return
  print(ans)

resolve()


if __name__ == "__main__":
    unittest.main()
