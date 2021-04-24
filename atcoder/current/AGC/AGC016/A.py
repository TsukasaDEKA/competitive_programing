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
        input = """serval"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """jackal"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """zzz"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """whbrjpjyhsrywlqjxdbrbaomnw"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 例 1 は r でもできる
  # serval
  # srral
  # rrrl
  # rrr
  # jackal
  # aakaa
  # aaaa
  # 例 3 (r で検索してハイライトすると動きがわかりやすい。)
  # whbrjpjyhsrywlqjxdbrbaomnw
  # whrrpjyhsrrwlqjxdbrraomnw
  # wrrrjyhsrrrlqjxdbrrromnw
  # rrrryhsrrrrqjxdbrrrrmnw
  # rrrrysrrrrrjxdbrrrrrnw
  # rrrrsrrrrrrxdbrrrrrrw
  # rrrrrrrrrrrdbrrrrrrr
  # rrrrrrrrrrrbrrrrrrr
  # rrrrrrrrrrrrrrrrrr
  # 特定の文字で S を区切った時、最長部分列の長さが答えっぽい。

  S = list(input())
  # 集計してみる
  collections = {}
  for i in range(len(S)):
    if S[i] not in collections: collections[S[i]] = [i]
    else: collections[S[i]].append(i)
  ans = inf
  for value in collections.values():
    temp_ans = value[0]
    for i in range(len(value)-1):
      temp_ans = max(temp_ans, value[i+1]-value[i]-1)
    temp_ans = max(temp_ans, len(S)-value[-1]-1)

    ans = min(ans, temp_ans)

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
