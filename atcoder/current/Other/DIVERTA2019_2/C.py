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
        input = """3
1 -1 2"""
        output = """4
-1 1
2 -2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 1 1"""
        output = """1
1 1
1 0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
0 1 2 3 4"""
        output = """10
0 1
-1 2
-3 3
4 -6"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5
-4 -3 -2 -1 0"""
        output = """10
0 -4
4 -3
7 -2
9 -1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """5
-4 -3 0 1 2"""
        output = """10
2 -3
-4 0
-4 1
5 -5"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 最後に、最も小さい値と最も大きい値を作りたい。
  # 正の最大値と負の最小値を一つずつ選んで、そこに統合していく形にすると良さそう。
  # ある程度の範囲で任意の個数の数字の符号を反転できる足し算っぽい
  # 符号を反転できる最大個数は N - 1 個で、最小が・・・1個？(多分)
  # 1 個以上、N - 1 個未満の符号を反転させる足し算であることがわかったので、あとはそれをどの順番でやるか考える。
  # 何となく優先度つきキューでいけそうな気がする。
  # 最小値が正だったら最大値以外を最小からひいていって、最後にそれを最大値から引く。
  # 最大値が負だったら、最大値から他の数字を順に引いていく
  # 最小値が負で最大値が正だったら、順に取り出していって、
  # 取り出した値が正だったら最小値から引く、取り出した値が負だったら最大値から引くと言うのを繰り返す。
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  max_A = A[-1]
  min_A = A[0]

  ans = []
  if min_A >= 0:
    for a in A[1:-1]:
      ans.append((min_A, a))
      min_A -= a
    ans.append((max_A, min_A))
    max_A -= min_A
  elif max_A <= 0:
    for a in A[:-1]:
      ans.append((max_A, a))
      max_A -= a
  else:
    for a in A[1:-1]:
      if a >= 0:
        ans.append((min_A, a))
        min_A -= a
      else:
        ans.append((max_A, a))
        max_A -= a
    ans.append((max_A, min_A))
    max_A -= min_A

  print(max_A)
  for a in ans:
    print(*a)


resolve()

if __name__ == "__main__":
    unittest.main()
