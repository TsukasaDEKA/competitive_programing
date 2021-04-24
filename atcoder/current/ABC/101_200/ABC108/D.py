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
        input = """4"""
        output = """3 4
1 2 0
1 2 1
2 3 0
2 3 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7"""
        output = """3 6
1 2 0
1 2 1
2 3 0
2 3 2
1 3 6
2 3 4"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """15"""
    #     output = """"""
    #     self.assertIO(input, output)
#     def test_Sample_Input_1(self):
#         input = """4"""
#         output = """8 10
# 1 2 0
# 2 3 0
# 3 4 0
# 1 5 0
# 2 6 0
# 3 7 0
# 4 8 0
# 5 6 1
# 6 7 1
# 7 8 1"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """5"""
#         output = """5 7
# 1 2 0
# 2 3 1
# 3 4 0
# 4 5 0
# 2 4 0
# 1 3 3
# 3 5 1"""
#         self.assertIO(input, output)

def print_ans(answers, nodes_amount):
  print(nodes_amount, len(answers))
  for ans in answers:
    print(ans)

def resolve():
  L = int(input())-1
  # bit 化して扱う。
  bit_L = list(reversed([int(x) for x in list(bin(L)[2:])]))
  answers = []

  # Node の数
  nodes_amount = len(bit_L)

  for i in range(1, nodes_amount):
    answers.append("{0} {1} {2}".format(i, i+1, 0))
    answers.append("{0} {1} {2}".format(i, i+1, 2**(i-1)))

  # 下から見ていって最初に 0 になる Node にグラフを繋ぐ。
  current_index = 0
  while bit_L[current_index]:
    bit_L[current_index] = 0
    current_index += 1
    if current_index >= len(bit_L):
      # 0が無ければ Node を追加して終了
      nodes_amount += 1
      answers.append("{0} {1} {2}".format(nodes_amount-1, nodes_amount, 0))
      answers.append("{0} {1} {2}".format(nodes_amount-1, nodes_amount, 2**(nodes_amount-2)))
      print_ans(answers, nodes_amount)
      return True

  L = 0
  for i, bit in enumerate(bit_L):
    L+=bit*(2**i)
  answers.append("{0} {1} {2}".format(current_index+1, len(bit_L), L))

  # 1 が見つかる度にその Node に接続する。
  for i in range(current_index, len(bit_L)):
    if bit_L[i]:
      bit_L[i] = 0
      L = 0
      for j, bit in enumerate(bit_L): L+=bit*(2**j)
      if(L==0):break
      answers.append("{0} {1} {2}".format(i+1, len(bit_L), L))
  print_ans(answers, nodes_amount)

resolve()

if __name__ == "__main__":
    unittest.main()
