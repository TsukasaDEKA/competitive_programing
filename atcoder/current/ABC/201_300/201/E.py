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
        input = """3
1 2 1
1 3 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 5 2
2 3 2
1 5 1
4 5 13"""
        output = """62"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
5 7 459221860242673109
6 8 248001948488076933
3 5 371922579800289138
2 5 773108338386747788
6 10 181747352791505823
1 3 803225386673329326
7 8 139939802736535485
9 10 657980865814127926
2 4 146378247587539124"""
        output = """241240228"""
        self.assertIO(input, output)

def resolve():
  # 経路を一個増やす時、今までの値 ^ 新しい経路の重みをすれば良い。
  # DFS をやりながらでできそう？
  # 累積 XOR みたいな感じで・・・
  # O(N**2)か
  # もうちょっと工夫が必要。
  # 全部の和の中に、 wi で括れるやつが存在するはず。
  # その中に wi+1 で括れるやつが存在するはず。しない？する場合もある。
  # 部分木で考えるとわかりやすいか？
  # DFS で帰り際に値を蓄積しておけばいけそう。
  inf = 10**18+1
  N = int(input())


  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
