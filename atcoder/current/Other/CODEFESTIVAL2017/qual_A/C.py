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
        input = """3 4
aabb
aabb
aacc"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
aa
bb"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 1
t
w
e
e
t"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2 5
abxba
abyba"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """1 1
z"""
        output = """Yes"""
        self.assertIO(input, output)

from collections import Counter
def resolve():
  inf = 10**10+1
  # 各文字の出現回数を集計する。
  # 回文が作成できる条件が、行 (列) が偶数個の場合、各文字が全て偶数個ないといけない。行 (列)が奇数個の場合、真ん中にくる文字だけ奇数個でも大丈夫
  # W、H の偶奇で場合分けして解ける？？？
  # サンプルを見てるとなかなか難しそう。H, W <= 100 なのでそれを利用して・・・？いや無理か
  # 角にある文字を置いた時、全部の行列が条件を満たす為には min(2, H)*min(2, W) 個同じ文字が必要。
  # 条件を満たせる文字で埋めてって、満たせなくなったら No、最終的に埋めれたら Yes？
  # 実装辛め。もっと簡単にいける方法欲しい。
  # W, H が両方とも奇数の場合、中心に 1 文字置く必要があるので、1 種類の文字だけ奇数で残りが全て偶数
  # W, H の片方が奇数の場合、奇数が含まれていると成り立たない。また、H//2*W//2 個分 同じ種類で 4 個の文字が取れないといけない。 (他の場合も一緒)
  # W, H が両方とも偶数の場合、全ての文字が 4 の倍数じゃないといけない。(H//2*W//2 個分 同じ種類で 4 個の文字が取れないといけないという条件に含まれる。)
  H, W = map(int, input().split(" "))
  A = [list(input()) for _ in range(H)]
  count_alphabet = {}
  for h in range(H):
    for w in range(W):
      if A[h][w] in count_alphabet: count_alphabet[A[h][w]]+=1
      else: count_alphabet[A[h][w]]=1

  minimum_4 = (H//2)*(W//2)
  count_4 = 0
  count_odd = 0
  for value in count_alphabet.values():
    if value>=4: count_4+=value//4
    if value%2: count_odd+=1

  if minimum_4 > count_4:
    print("No")
    return

  if W%2 and H%2:
    if count_odd!=1:
      print("No")
      return
  elif count_odd!=0:
    print("No")
    return

  print("Yes")

resolve()

if __name__ == "__main__":
    unittest.main()
