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

    def test_入力例_1(self):
        input = """UL?
1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """UD?
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """UUUU?DDR?LLLL
1"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """UULL?
2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """UULL?
2"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
  # ドローンの移動について、どの順番で行うかは重要ではない。
  # T = 1 の時は ? 以外での移動後のマンハッタン距離に ? の個数を追加して、
  # T = 2 の時は移動後のマンハッタン距離から ? の個数を引いて、負だった場合、その値が偶数か奇数かで出力をかえる。
  S = list(input())
  T = int(input())

  x = 0
  y = 0
  questions = 0
  for s in S:
    if s == "?":questions+=1
    elif s== "U": y+=1
    elif s== "D": y-=1
    elif s== "R": x+=1
    elif s== "L": x-=1
  
  if T==1:
    print(abs(x)+abs(y)+questions)
  else:
    ans = abs(x)+abs(y)-questions
    if ans < 0: ans = abs(ans)%2
    print(ans)

resolve()


if __name__ == "__main__":
    unittest.main()
