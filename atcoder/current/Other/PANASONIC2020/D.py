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
        input = """1"""
        output = """a"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2"""
        output = """aa
ab"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3"""
        output = """aaa
aab
aba
abb
abc"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4"""
        output = """aaaa
aaab
aaba
aabb
aabc
abaa
abab
abac
abba
abbb
abbc
abca
abcb
abcc
abcd"""
        self.assertIO(input, output)


alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+96)

def resolve():
  # 例えば abcb は標準形で acbc は標準形では無い。
  # i < j の時、S[0 ~ i] までの辞書順最大値に 1 加えた物が S[j] の辞書順最大値になる
  # a=1, b=2,・・・j=10 と置き桁上がり計算をしていく。
  # aaaab は標準形で aaaac は標準形では無い aaaba, aaabb, aaabc は標準形で aaabd は標準形では無い。
  # 答えの数は N! 個 (< 3.6*10**6)未満になるけど、計算速度的にどうだろ。
  N = int(input())

  if N==1:
    print("a")
    return
  ans = [1]*N
  max_val = [1]*N
  while True:
    # 出力
    print(*[num2alpha(x) for x in ans], sep="")
    # 条件を満たすようにインクリメント
    # ans[:i+1]の最大値
    for i in range(1, N-1):
      max_val[i]=max(max_val[i-1], ans[i])
    ans[-1]+=1
    i=N-1
    while ans[i] > max_val[i-1]+1:
      ans[i]=1
      i-=1
      if i==0: return
      ans[i]+=1

resolve()

if __name__ == "__main__":
    unittest.main()
