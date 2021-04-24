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
        input = """issii
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """qq
81"""
        output = """81"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """cooooooooonteeeeeeeeeest
999993333"""
        output = """8999939997"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter
  # |S| が小さい。K が大きい
  # 先頭と末尾が同じ時、繰り返しによって文字の連続が発生する。
  # N 文字連続している時に、その N 文字を連続しないようにする操作回数は N//2
  # 先頭と末尾が同じかつ連続してる文字数が足して偶数だったら (操作回数 + 1)*K - 1 が答え
  # そうでなければ操作回数*K が答え
  S = list(input())
  K = int(input())

  count_S = Counter(S)
  # 全部同じ文字だった場合
  if len(count_S) == 1:
    # オーバーフローとか大丈夫か？
    print(K*len(S)//2)
    return

  count = 1
  operation = 0
  for i in range(1, len(S)):
    if S[i-1] != S[i]:
      operation+=count//2
      count = 1
      continue
    count+=1
  operation+=count//2

  # 全部同じ文字である可能性は排除してあるので安心してカウントできる。
  if S[0] == S[-1]:
    top = 1
    i = 1
    while S[i] == S[0]:
      i += 1
      top += 1

    i = len(S)-2
    tail = 1
    while S[i] == S[-1]:
      i -= 1
      tail += 1

    if (top+tail)%2==0:
      print((operation+1)*K - 1)
      return
  print(operation*K)

resolve()

if __name__ == "__main__":
    unittest.main()
