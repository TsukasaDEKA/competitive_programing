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
        input = """4 3
1 3 4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 21
1050624 32772 493952 144 869120"""
        output = """869120"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20 60
216181578206878016 81348488767472704 26388280246272 281543729742896 72127981178847488 2199108462600 585610888171487234 22027813536776 567459673280576 146648462866649600 144484898860704776 576471786208755714 4398621196432 144141576657960976 81069330992726040 360851057582278674 17859112 11570646360064 144115206396936193 1702052723957760"""
        output = """977902973481140224"""
        self.assertIO(input, output)

def resolve():
  # 二進数で 60 桁の数値を扱う。
  # N <= 20 の全ての Ai について x のビットごとの論理積が 0 でないってことは、
  # A1 の内、1 が立ってる桁の少なくともどれかは 1 になっている x を見つける必要があるという事になる。
  # 例 1 の入力を二進数にすると↓のようになって、右端を 1 桁目として 1, 3 桁目を同時に選択した場合条件を満たし、
  # 2 桁目を選ぶ選ばないで 2 パターンが答えになる。
  # - 001
  # - 011
  # - 100
  # - 101

  # 1111
  # 1001
  # 1010
  # 1111
  # 左端を選び、残りの桁を自由にえ

  N, D = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  print()
  for i in range(N):
    print(bin(A[i])[2:].zfill(D))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()