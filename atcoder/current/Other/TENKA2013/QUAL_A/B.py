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
        input = """7 20
Push 2 3
Push 4 5
Top
Size
Pop 5
Top
Size"""
        output = """5
6
3
1
SAFE"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 10
Push 40 40"""
        output = """FULL"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 10
Push 1 2
Top
Pop 1
Top
Size"""
        output = """2
EMPTY"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4 10
Top
Size
Push 1 1
Top"""
        output = """EMPTY"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """7 20
Push 2 3
Push 4 5
Top
Size
Pop 3
Top
Size"""
        output = """5
6
5
3
SAFE"""
        self.assertIO(input, output)

def resolve():
  # 普通にスタックの処理をシミュレ0ちすれば所作そうだけどどうなんだろう。
  # N が 10**5 もあるので、シミュレートすると厳しそう。
  # ~~先頭要素と要素数だけ管理する。~~
  # 「先頭要素」を勘違いしてた。先頭は最後に入れた要素。
  from collections import deque
  Q, L = map(int, input().split(" "))
  stack = deque()
  count = 0
  for _ in range(Q):
    query = input().split(" ")
    if query[0] == "Push":
      N, M = map(int, query[1:])
      count += N
      stack.append((M,N))
      if count > L:
        print("FULL")
        return
    elif query[0] == "Pop":
      N = int(query[1])
      count -= N
      if count < 0:
        print("EMPTY")
        return
      while N > 0:
        m, n = stack.pop()
        N -= n
        if N < 0: stack.append((m, -N))
    elif query[0] == "Top":
      if count <= 0:
        print("EMPTY")
        return
      print(stack[-1][0])
    else:
      print(count)
    
  print("SAFE")

# resolve()

if __name__ == "__main__":
    unittest.main()
