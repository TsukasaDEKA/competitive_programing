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
        input = """1
12 3 69853"""
        output = """69853"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
7 3 200000
3 2 100000
5 3 150000"""
        output = """350000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
376 640 602876667
4015 1868 533609371
3330 152 408704870
1874 798 30417810
2 1450 40706045
3344 1840 801881841
2853 1229 5235900
458 1277 997429858"""
        output = """1744196082"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20
376 640 602876667
4015 868 533609371
3330 152 408704870
1874 798 30417810
2 450 40706045
3344 840 801881841
2853 229 5235900
458 277 997429858
1689 948 981897272
4774 393 997361572
4237 750 294800444
4663 293 277667068
2249 808 444906878
3341 137 845317003
3625 765 739689211
911 510 326127348
1343 193 235655766
842 323 406413067
1425 303 68833418
212 808 745744264"""
        output = """6583558066"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """30
376 140 602876667
4015 368 533609371
3330 152 408704870
1874 298 30417810
2 450 40706045
3344 340 801881841
2853 229 5235900
458 277 997429858
1689 448 981897272
4774 393 997361572
4237 250 294800444
4663 293 277667068
2249 308 444906878
3341 137 845317003
3625 265 739689211
911 10 326127348
1343 193 235655766
842 323 406413067
1425 303 68833418
212 308 745744264
3563 376 196296968
4186 323 275217640
332 361 337078801
4466 245 694789156
3763 250 432518459
2937 124 581390864
2255 227 642944345
2851 480 688009163
1957 295 5532462
3277 445 15791361"""
        output = """11420667389"""
        self.assertIO(input, output)

def resolve():
  # D-C, D を単純に並べていくと仕事をしている期間に重なりがあることがわかる。
  # 仕事をする期間は前にずらすことができる。
  # 重ならないように上手くずらしたい。
  # 一旦ソートする必要はありそう。
  # N <= 20 なら全探索
  # dp[i][d] := i 番目までの仕事を取った場合
  inf = 10**18+1
  N = int(input())
  A = sorted([list(map(int, input().split(" "))) for _ in range(N)])
  max_d = 5001
  dp = [0]*max_d
  # dp = [0]*5001
  for i in range(N):
    d, c, s = A[i]
    for j in reversed(range(c, d+1)):
      dp[j] = max(dp[j], dp[j-c]+s)
    for j in range(d+1, max_d):
      dp[j] = max(dp[j], dp[j-1])

  # print(dp)
  print(dp[-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
