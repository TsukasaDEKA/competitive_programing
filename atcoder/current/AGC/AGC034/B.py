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
        input = """ABCABC"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """C"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """ABCACCBABCBCAABCB"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  S = input()
  # S の頭から T の末尾にコピーしていって、T の末尾が A だったら . に、BC だったら # に置き換える。
  # T を頭から見ていって、. の数を数える。# が見つかったら ans+=<.の数> をする。
  # . や # 以外の文字が見つかったら . のカウントをリセットする。N=len(s) とすると O(N+N)
  T = "_"
  for s in S:
    if T[-1]=="B" and s == "C":
      T=T[:-1]+"#"
    else:
      T+=s

  ans=0
  A_count=0
  for t in T:
    if t=="#":
      ans+=A_count
      continue
    if t=="A":
      A_count+=1
      continue
    A_count=0
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
