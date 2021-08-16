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

    # def test_Sample_Input_1(self):
    #     input = """oxoxx"""
    #     output = """3"""
    #     self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """oxxxxoooo"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """ox"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """o"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """xxxoxo"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """xxoooxxxxx"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_7(self):
        input = """oo"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_8(self):
        input = """ooo"""
        output = """1"""
        self.assertIO(input, output)

    # def test_Sample_Input_1(self):
    #     input = """xxxxoxo"""
    #     output = """4"""
    #     self.assertIO(input, output)


def resolve():
  popcnt = lambda x: bin(x).count("1")

  # S は bit で表現した方が楽そう。(or 演算もできるし。)
  # 組み合わせ数は 2**10 程度なので全探索でいける。
  S = list(input())
  N = len(S)
  
  S_bit = 0
  for i in range(N):
    if S[i] == "o":
      S_bit += 1<<i

  ans_check = (1<<N)-1
  # print(bin(ans_check))
  ans = N+1
  for bit in range(ans_check+1):
    temp_ans = S_bit
    for b in range(N):
      if (bit>>b)&1:
        temp_bit = ((S_bit<<(b+1))&ans_check) | S_bit>>(N-(b+1))
        # print(bin((S_bit<<(b+1))&ans_check), bin(S_bit>>(N-(b+1))))
        temp_ans |= temp_bit

    for i in range(temp_ans.bit_length()+1):
      if (ans_check&(temp_ans>>i)) == ans_check:
        break
    else:
      continue

    # print(bin(temp_ans), bin(ans_check), bin(ans_check), popcnt(bit))
    if ans > popcnt(bit)+1:
      ans = popcnt(bit)+1
      # for b in range(N):
      #   if (bit>>b)&1:
          # print('bin: {:020b}'.format(S_bit<<b))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
  unittest.main()