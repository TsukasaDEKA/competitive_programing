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
        input = """3 3 1 1"""
        output = """100
010
001"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 5 2 0"""
        output = """01010"""
        self.assertIO(input, output)

def resolve():
  H, W, A, B = map(int, input().split(" "))
  # 「少ない方がA(orB)」を満たせないパターン
  if H//2 < B or W//2 < A:
    print("No")
    return
  # 行列演算っぽくできないか？
  column = [1]*H
  for i in range(B): column[i]*=-1
  row = [1]*W
  for i in range(A): row[i]*=-1

  ans=[[0]*W for _ in range(H)]
  for h in range(H):
    for w in range(W):
      ans[h][w] = 1 if column[h]*row[w]==1 else 0
    print(*ans[h], sep="")

resolve()


if __name__ == "__main__":
    unittest.main()
