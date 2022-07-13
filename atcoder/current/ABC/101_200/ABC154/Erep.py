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

    def test_Sample_Input_1(self):
        input = """100
1"""
        output = """19"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """25
2"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314159
2"""
        output = """937"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
3"""
        output = """117879300"""
        self.assertIO(input, output)

def resolve():
  from scipy.special import comb
  # K がとても小さい
  inf = 10**18+1
  S = input()
  lenS = len(S)
  K = int(input())

  # 場合分けが大変なので N が小さい時は全探索
  if lenS < 7:
    N = int(S)
    ans = 0
    for i in range(1, N+1):
      s_i = str(i)
      if len(s_i) - s_i.count("0") == K:
        ans += 1
    print(ans)
  else:
    # 先頭から 3 桁とって 0 の個数と残りの桁数で考える。
    ans = 0
    headS = int(S[:3])
    for i in range(headS):
      s_i = str(i)
      k = K - (len(s_i) - s_i.count("0"))
      if k < 0: continue
      if k == 0:
        ans += 1
        continue
      ans += comb(lenS-3, k, exact=True)*pow(9, k)

    s_i = S[:3]
    k = K - (len(s_i) - s_i.count("0"))
    if k == 0: ans += 1
    if k == 1:
      S = list(S)
      for i in range(3, lenS):
        if S[i] != "0":
          ans += int(S[i])
          ans += (lenS-1-i)*9
          break
    if k == 2:
      S = list(S)
      for i in range(3, lenS-1):
        if S[i] != "0":
          # i 番目を S[i] にする場合
          for j in range(i+1, lenS):
            if S[j] != "0":
              ans += int(S[j])
              ans += (lenS-1-j)*9
          # i 番目を 1 ~ S[i]-1 にする場合
          ans += (int(S[i])-1)*(lenS-1-i)*9
          # i 番目を 0 にする場合
          ans += comb(lenS-1-i, k, exact=True)*pow(9, k)
          break

    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()