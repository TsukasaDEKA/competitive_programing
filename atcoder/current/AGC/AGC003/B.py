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
4
0
3
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8
2
0
1
6
0
8
2
1"""
        output = """9"""
        self.assertIO(input, output)


    def test_Sample_Input_3(self):
        input = """7
2
1
2
8
1
2
1"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  # 順にペアにしていけば良いのでは・・・？そんな簡単なはずない？
  # 順にペアにしていく方針だとダメだった。テストケース考えてみる。
  # この方針だと、A=[2 1 2 1] で 2 ペアしか作れない (実際は最大 3 ペア)
  # 奇数で挟まれてて真ん中が偶数の場合、左右から先に取って、残り偶数を取った方が多くペアが作れる。
  # 可能な限り奇数カードを最小化したい。
  # 左から順にカードを見ていって、奇数かつ隣が 0 より大きかったら取る。
  N = int(input())
  A = [int(input()) for _ in range(N)]

  # まず、奇数を潰していく。
  ans = 0
  for i in range(N-1):
    if A[i]%2 and A[i+1]:
      ans+=1
      A[i]-=1
      A[i+1]-=1
  # print(*A)
  # 余ったカードでペアを作る。
  for i in range(N):
    ans+=A[i]//2
    A[i]%=2

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
