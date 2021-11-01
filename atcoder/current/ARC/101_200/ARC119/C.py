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
        input = """5
5 8 8 6 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
12 8 11 3 3 13 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
8 6 3 9 5 4 7 2 1 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """14
630551244 683685976 249199599 863395255 667330388 617766025 564631293 614195656 944865979 277535591 390222868 527065404 136842536 971731491"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ
  from collections import Counter

  # どちらの操作を行っても、偶数番目の数の合計と奇数番目の数の変化は等しい。
  # l, r を選んだ時に 偶数番目と奇数番目の和の数が等しくなる l, r　の組み合わせが知りたい。
  # 累積和でいけそうだけど、l, r の選び方は N**2 個あるので間に合わないかも？
  # 偶数番目を正負逆転させて、累積和をとる。
  # 累積和した結果が同じ数字の場合、その区間の和が 0 になることになるので、その区間は条件を満たす。
  # 累積和した配列上で同じ数字を 2 個とる取り方が何パターンあるか計算して足し合わせれば良い。
  N = int(input())
  # 偶数番目を反転
  A = [((-1)**(i%2))*int(x) for i, x in enumerate(input().split(" "))]
  # 同じ数字毎に個数を集計
  agg = Counter([0]+list(accumulate(A)))

  # 同じ数字を 2 個選ぶパターンの数は n = <同じ数字の個数> とした時、 nC2。
  # 全ての数字に対してそれを足し合わせる。
  ans = 0
  for v in agg.values():
    ans+=(v*(v-1))//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
