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
  # 最初から同じ高さである組み合わせであれば目的を達成できる。
  # シミュレーションしてたら間に合わない。
  # 区間の端は行う操作が少なめになる。
  # X, 2*X, X みたいな並びは目標を達成できる。
  # X, X+(X-Y), Y みたいな並びも同様
  # 入力例 2 はいろんな手法の合わせ技になっている。
  # l と r の選び方は N*(N-1)/2 通りある。
  # 全部探索していったら間に合わない。
  # 3 9 5 4 7 2
  # 区間の端は必ず引くだけしかできない。

  N = int(input())
  A = [int(x) for x in input().split(" ")]



import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
