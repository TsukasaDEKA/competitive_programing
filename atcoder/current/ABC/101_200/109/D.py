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
        input = """2 3
1 2 3
0 1 1"""
        output = """3
2 2 2 3
1 1 1 2
1 3 1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
1 0
2 1
1 0"""
        output = """3
1 1 1 2
1 2 2 2
3 1 3 2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 5
9 9 9 9 9"""
        output = """2
1 1 1 2
1 3 1 4"""
        self.assertIO(input, output)

def resolve():
  # 一行を1 ~ H-1 まで順に見ていって、奇数だったら右に一個移動するようにする。
  # 下の行に移動しても同じようにする。
  # 全部の行でそれを実行したら、右端を縦に見ていく。
  # 奇数のコインが溜まっているはずなので、同じ様に、1 ~ W-1まで順に見ていって、奇数だったら下に一個移動する様にする。
  # 500**2 なので間に合う
  H, W = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]
  ans = []
  for h in range(H):
    for w in range(W-1):
      if A[h][w]%2:
        ans.append((h+1, w+1, h+1, w+2))
        A[h][w]-=1
        A[h][w+1]+=1
  
  for h in range(H-1):
    if A[h][W-1]%2:
      ans.append((h+1, W, h+2, W))
      A[h][W-1]-=1
      A[h+1][W-1]+=1

  print(len(ans))
  for a in ans:
    print(*a)

resolve()

if __name__ == "__main__":
    unittest.main()
