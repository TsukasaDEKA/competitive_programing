import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """7 3
atcoder"""
        output = """acd"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14 5
kittyonyourlap"""
        output = """inlap"""
        self.assertIO(input, output)


def resolve():
  alpha2num = lambda c: ord(c) - ord('a')
  num2alpha = lambda c: chr(c+97)

  inf = 10**18+1
  N, K = map(int, input().split(" "))
  S = list(input())
  dictionary = [[-1]*26 for _ in range(N)]
  dictionary[-1][alpha2num(S[-1])] = N-1
  for i in range(N-2, -1, -1):
    tar = alpha2num(S[i])
    dict_i = dictionary[i]
    for j in range(26):
      if j == tar:
        dict_i[j] = i
      else:
        dict_i[j] = dictionary[i+1][j]
  # k 文字目に選ぶ文字を決める。
  ans = [""]*K
  current_i = 0
  for k in range(K):
    # a から順に見ていって、0 以上かつその文字を取った場合に残りの文字を取り切れるようだったら採用。
    dict_c = dictionary[current_i]
    for i in range(26):
      if dict_c[i] >= 0 and N - dict_c[i] >= K-k:
        ans[k] = num2alpha(i)
        current_i = dict_c[i]+1
        break

  print("".join(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
