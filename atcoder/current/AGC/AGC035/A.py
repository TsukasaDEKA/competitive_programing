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
1 2 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 2 4 8"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  # N <= 10**5 なのがちょっと厳しい。
  # 並べ方は (N-1)! くらい？なので前探索だと到底間に合わない。
  
  # なぜかわからないけど ans == 0 or not で殆ど通ってしまう。
  # after_contest で引っかかってるので、N の偶奇とかそこらへんで条件分岐が必要そう。
  # N == 4 の場合、対角のラクダ同士が同じ値の帽子をかぶってなくてはいけないので、全部 0 じゃないと成り立たない。
  # after_contest はもう一個あるので、多分奇数個の場合に考慮抜けがある。
  # 0, 0, 1, 2, 3 は全ての xor をとると 0 になるけど、答えは No になる。
  # 4, 4, 1, 2, 3 は全ての xor をとると 0 になるけど、答えは No になる。
  # 偶数個の場合、[2]*6 を全て xor すると 0　になるが、答えは No になる。
  # 反例がたくさんありそう。
  # Xi-1, Xi, Xi+1 を見る場合、Xi-1 ^ Xi+1 == Xi なので、Xi-1 ^ Xi　^ Xi+1 == 0
  # Xi+1 を中心に見ると、Xi ^ Xi+2 == Xi+1 なので Xi ^ Xi+1 ^ Xi+2 == 0 じゃなきゃいけなくて、結果、 Xi+2 == Xi-1 になる。
  # 同じように Xi+3 == Xi になる。これを繰り返していくと、A は 3 種類の数字でる必要があり、
  # その 3 種類の数字を X3i ^ X3i+1 ^ X3i+2 == 0という形に並べられないといけない。
  # また、ループしていることを考えると、全部の数字が 0 じゃないかぎり、N は 3 の倍数じゃなきゃいけない。
  # 0, 2, 2, 0, 2, 2 でも大丈夫っぽい？ 3 種類の数字のうち、2 種類が同値でも OK

  from collections import defaultdict
  N = int(input())
  A = list(map(int, input().split(" ")))
  count = defaultdict(int)
  for a in A: count[a] += 1
 
  keys = sorted(count.keys())
  if count[0] == N:
    print("Yes")
    return

  if keys[0] == 0 and count[0] == N//3 and count[keys[1]] == (2*N)//3:
    print("Yes")
    return

  if count[keys[0]] == N//3 and count[keys[1]] == N//3 and count[keys[2]] == N//3 and keys[0]^keys[1]^keys[2] == 0:
    print("Yes")
    return
  print("No")
resolve()

if __name__ == "__main__":
    unittest.main()
