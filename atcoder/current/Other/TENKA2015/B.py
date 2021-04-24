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

    def test_入力例1(self):
        input = """{1:2}"""
        output = """dict"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """{1,2}"""
        output = """set"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """{}"""
        output = """dict"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """{{{1:2}:{}}, {}}"""
        output = """set"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """{{}}"""
        output = """set"""
        self.assertIO(input, output)

def resolve():
  # {{1:2}} は SET
  # {{1:2}:{}} は DICT
  # {{{1:2}:{}}, {}} は SET
  # 単純に前から見ていったのでは判別できないので、何かしらの方法を考えなきゃいけない。
  # スタックで、{ が見つかったら要素を追加、ってしていけばなんかできそう。
  from collections import deque
  S = list(input())
  stack = deque()

  # 外周以外の括弧とその中身を全部消す。
  for s in S[:-1]:
    if s == "{":
      stack.append("{")
      continue

    last_element = stack.pop()
    if s == "}":
      stack[-1]+=","
      continue
    if s != ":": s = ","
    stack.append(last_element+s)

  tar = stack.pop()
  is_colon_in = ":" in tar
  is_comma_in = "," in tar
  if not is_colon_in and is_comma_in:
    print("set")
    return
  print("dict")
resolve()

if __name__ == "__main__":
    unittest.main()
