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
        input = """2
1
01
01
10
2
0101
0011
1100"""
        output = """010
11011"""
        self.assertIO(input, output)

def resolve():
  # "1"*N + "0" + "1"*N で全てが片付くと思ったけど、これだと
  # 1001 + 1001 のようなのが混じっていた場合に落ちる。
  # S1 = 0110 + 0110 S2 = 1001 + 1001 
  # 答えの 0、1 が混じりあうと、どうしても 1 の右側に 0 が無いパターンや、 0 の右側に 1 が無いパターンでどうしても詰まる。
  # なので、連続した 1 とか 0 を取れないかを考えた。
  # N=2 の時に考えられるパターンは以下の通り。
  # 00110011
  # 01010101
  # 10011001
  # 10101010
  # 11001100
  # ここで、連続した 1 を取る時に、確実に左右に 0 が残る取り方が存在する事がわかる。
  # さらに考えると、最も左側の 0 から右側にある 1 を N 個取って、その後に 0 を N 個取れる事にも気づく
  # なので答えは "0" + "1"*N + "0"*N
  T = int(input())
  for _ in range(T):
    N = int(input())
    _  = [input() for _ in range(3)]
    print("0" + "1"*N + "0"*N)

resolve()

if __name__ == "__main__":
    unittest.main()
