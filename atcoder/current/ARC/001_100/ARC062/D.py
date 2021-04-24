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
        input = """gpg"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """ggppgggpgg"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  # グーより多くパーは出せない。
  # グーとパーの個数を数えて、相手がグーを出す時にパーを出せたら出す・・・でいける？
  # その場合だと結局トントンになるか？
  count_g = 0
  count_p = 0
  ans = 0

  for s in S:
    if count_g > count_p:
      count_p += 1
      if s == "g": ans+=1
    else:
      count_g += 1
      if s == "p": ans-=1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
