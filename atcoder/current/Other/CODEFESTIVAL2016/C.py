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
        input = """xyz
4"""
        output = """aya"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """a
25"""
        output = """z"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """codefestival
100"""
        output = """aaaafeaaivap"""
        self.assertIO(input, output)

def resolve():
  # 可能な限り先頭から a にしたい。可能な限りの文字を a にした後、余った分は末尾で消化する。
  S = list(input())
  K = int(input())
  num2alpha = lambda c: chr(c+97)
  alpha2num = lambda c: ord(c) - ord('a')
  # deepcopy した方がいいかも
  ans = [""]*len(S)
  # S を先頭から見ていって、K の残り回数で a にできるなら a にする。できないなら次の文字をみる。
  # 最後に余った K を使って最後の文字を操作する。
  for i in range(len(S)):
    if 26 - alpha2num(S[i]) <= K and S[i] != "a":
      K-=26 - alpha2num(S[i])
      ans[i]="a"
    else:
      ans[i]=S[i]
  ans[-1] = num2alpha((alpha2num(ans[-1])+K)%26)
  print("".join(ans))

resolve()

if __name__ == "__main__":
    unittest.main()
