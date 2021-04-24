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

    def test_入力例1(self):
        input = """3 3
2
3
1"""
        output = """1
3
2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1
1
1"""
        output = """1
2
3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 10
3
1
4
1
5
9
2
6
5
3"""
        output = """3
5
6
2
9
1
4
7
8
10"""
        self.assertIO(input, output)

def resolve():
  # A を後ろから順に見ていって、出てきた数字にインデックスを貼っていく。
  # 既にインデックスが貼られていたら continue
  # A を最後まで見たあと、インデックスが貼られていない数字に順にインデックスを貼る。
  N, M = map(int, input().split(" "))
  A = [int(input())-1 for _ in range(M)]
  ans = [None]*N
  index = 0
  for a in reversed(A):
    if ans[a] is not None: continue
    ans[a] = index
    index += 1

  for i in range(N):
    if ans[i] is not None: continue
    ans[i] = index
    index+=1
  
  print(*[i+1 for _, i in sorted([(x, i)for i, x in enumerate(ans)])], sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
