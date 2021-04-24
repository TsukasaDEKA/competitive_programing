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

    def test_入力例_1(self):
        input = """abc aaa ababa abcba abc
2
abc
**a**"""
        output = """*** aaa ***** abcba ***"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aaaa aaa aaaaaa aaaa
3
a
aa
aaa"""
        output = """aaaa *** aaaaaa aaaa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """i have a pen
1
*"""
        output = """* have * pen"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """digital arts
1
digital*arts"""
        output = """digital arts"""
        self.assertIO(input, output)

def resolve():
  # S は1000文字以下なので、最大でも 500単語しかない。
  # N <= 50 なので 500*50 でも間に合う？
  # 各文字の一致を判定していったらちょっと厳しいかもしれないので少し工夫する。
  # NG ワードの文字数でフィルタリングしてみる。
  from collections import defaultdict

  S = input().split(" ")  
  N = int(input())
  T = defaultdict(list)
  for _ in range(N):
    t = input()
    T[len(t)].append(t)

  for i in range(len(S)):
    s = S[i]
    is_ng = False
    for t in T[len(s)]:
      match_count = 0
      for j in range(len(t)):
        if t[j] == "*" or t[j] == s[j]:
          match_count+=1
          continue
        break
      if match_count == len(t):
        is_ng = True
        break
    if is_ng: S[i] = "*"*len(S[i])
  print(*S)

resolve()

if __name__ == "__main__":
    unittest.main()
