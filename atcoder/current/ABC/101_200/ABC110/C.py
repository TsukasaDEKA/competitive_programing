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
        input = """azzel
apple"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """chokudai
redcoder"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """abcdefghijklmnopqrstuvwxyz
ibyhqfrekavclxjstdwgpzmonu"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  T = list(input())

  # S と T で同じインデックスであれば同一文字がある位置も同じであるかどうかを確認する。
  # 出現した文字をキーとして、最初に出てきたインデックスを記録しておく。検索 O(1)
  S_index_dict = {}
  T_index_dict = {}
  for i in range(len(S)):
    if S[i] in S_index_dict:
      if T[S_index_dict[S[i]]] != T[i]:
        print("No")
        return
    else:
      S_index_dict[S[i]] = i
    
    if T[i] in T_index_dict:
      if S[T_index_dict[T[i]]] != S[i]:
        print("No")
        return
    else:
      T_index_dict[T[i]] = i
  print("Yes")
resolve()

if __name__ == "__main__":
    unittest.main()
