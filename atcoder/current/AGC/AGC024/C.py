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
        input = """4
0
1
1
2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1
2
1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9
0
1
1
0
1
2
2
1
2"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  # A(i)+1 >= A(i+1) である必要がある。
  # 階段状である時、([0, 1, 2, 3・・・]の時) 操作の最小回数は N-1 回になる。
  # A[0] は必ず 0 である必要がある。
  # [0, 1, 2, 3, 3, 3] の時、
  # [0, 0, 0, 1, 0, 0]
  # [0, 0, 0, 1, 2, 0]
  # [0, 0, 0, 1, 2, 3]
  # [0, 0, 1, 1, 2, 3]
  # [0, 0, 1, 2, 2, 3]
  # [0, 1, 1, 2, 3, 3]
  # [0, 1, 2, 2, 3, 3]
  # [0, 1, 2, 3, 3, 3] が最小手順
  # 制約の上では A(i) <= 10**9 だけど、実際のところ、A(i) < N になるはず。
  # 末尾から見ていって、実際にシミュレーションすることで答えが出せそう。
  # TLE した。
  # 愚直にシミュレーションしなくても良さそう。
  # A[i] >= A[i+1] の状況だった場合だけ処理をすれば良い。
  N = int(input())
  A = [int(input()) for _ in range(N)]
  if A[-1] >= N:
    print(-1)
    return
  ans = A[-1]
  for i in reversed(range(N-1)):
    if A[i] > i or A[i]+1 < A[i+1]:
      print(-1)
      return
    if A[i] >= A[i+1]: ans+=A[i]

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
