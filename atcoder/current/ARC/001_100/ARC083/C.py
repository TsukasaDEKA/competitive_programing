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
        input = """1 2 10 20 15 200"""
        output = """110 10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 2 1 2 100 1000"""
        output = """200 100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """17 19 22 26 55 2802"""
        output = """2634 934"""
        self.assertIO(input, output)

def resolve():
  # F <= 3000 なので、A, B の選べるパターンは少ない。(30 最大で 30 パターンしかなくて、それを A, B の組み合わせで実現できるか判定すれば良い。)

  # なので、全てのパターンを網羅してもいけそう。
  # 操作 3, 4 をどれだけ行うかが問題だけど、F - (A+B)*100 か E*(A+B) を最小値にした二次方程式を解いて、
  # 答えが整数になった場合、それを仮の答えとし、仮の答えの中から最大値を選べば良い。
  # E <= 100 なので E*(F//100) は最大でも 3000.
  # E を 1 ずつ減らしていけば良くて、450*3000 でざっくり 1350000 < 2*10**6 程度にしかならない。
  A, B, C, D, E, F = map(int, input().split(" "))

  ans_water = 100*A
  ans_suger = 0
  max_concentration = 0
  for f in range(A, (F//100) + 1):
    is_correct = False
    for b in range(f//B+1):
      if (f - b*B)%A==0:
        is_correct = True
        break
    if not is_correct: continue

    max_suger = min(f*E, F-f*100)
    for suger in reversed(range(1, max_suger+1)):
      if max_concentration > 100*suger/(f*100+suger): break
      for d in range(suger//D+1):
        if (suger - d*D)%C==0:
          max_concentration = 100*suger/(f*100+suger)
          ans_water = f*100
          ans_suger = suger
          if suger == f*E:
            print(ans_water+ans_suger, ans_suger)
            return
          break

  print(ans_water+ans_suger, ans_suger)

resolve()

if __name__ == "__main__":
    unittest.main()
