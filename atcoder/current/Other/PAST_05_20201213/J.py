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
        input = """ab2c1
6"""
        output = """b"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """atcoder
6"""
        output = """e"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """a999999999999999
# 1000000000000000"""
#         output = """a"""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """a99999999999
100000000000"""
        output = """a"""
        self.assertIO(input, output)
def resolve():
  # 愚直にやるとメモリーエラーになるので、インデックスだけ動かす。
  S = list(input())
  X = int(input())
  current_index = 0
  current_string_len = 0
  for s in S:
    if s.isdecimal():
      temp = current_index
      for _ in range(int(s)+1):
        if current_index+temp >= X:
          target = X-current_index
          T=""
          for s_ in S:
            if s_.isdecimal():
              temp_T = T
              for _ in range(int(s)+1):
                T+=temp_T
                if len(T)>=target:
                  print(T[target-1])
                  return
            else:
              T+=s_
            if len(T)>=target:
              # print(T, target)
              print(T[target-1])
              return

        current_index+=temp
    else:
      current_index+=1
  print(S[X-1])
resolve()

if __name__ == "__main__":
    unittest.main()
