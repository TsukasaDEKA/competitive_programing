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
        input = """6
icefox"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
firebox"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """48
ffoxoxuvgjyzmehmopfohrupffoxoxfofofoxffoxoxejffo"""
        output = """27"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """14
fofofofoxoxxxx"""
        output = """2"""
        self.assertIO(input, output)


from collections import deque

def resolve():
  N = int(input())
  S = list(input())

  # スタックを使って、f が出てきたら新規作成、次の文字はスタックの一番上に入れる、fox が完成したら除外というのを繰り返す。 O(N)
  fox_count = 0
  fox_stack = deque()
  for s in S:
    if s != "f" and s != "o" and s != "x":
      fox_stack.clear()
      continue

    if s == "f":
      fox_stack.append("f")
      continue

    if fox_stack:
      current_fox = fox_stack.pop()
      # print(current_fox)
      if current_fox[-1] == "f" and s == "o":
        current_fox+="o"
        fox_stack.append(current_fox)
        continue
      if current_fox[-1] == "o" and s == "x":
        fox_count+=1
        continue
      fox_stack.clear()

  print(N-3*fox_count)

resolve()

if __name__ == "__main__":
    unittest.main()
