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
1
2 1
1
1 1
1
2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
1
2 0
1
1 0"""
        output = """1"""
        self.assertIO(input, output)

from itertools import combinations

def resolve():
  # 総当たりだと N == 15 の時に 2**15 == 32768 なので O(N) とか O(logN) とかなら間に合いそう。
  # 毎回証言検索をしていると間に合わないので、「X さんに関する証言」でまとめると良い？？？
  # 2 次元配列にして、i さんは j さんのことを testimony[i][j] と言っている、というようなまとめ方をすると、各証言を O(1) で取ってこれる。
  N = int(input())

  testimony = [[None]*N for _ in range(N)]
  for i in range(N):
    A = int(input())
    for _ in range(A):
      X, Y = map(int, input().split(" "))
      X-=1
      testimony[i][X] = Y

  # 正直者が多い順から探索していって、証言に矛盾が発生しないことが確認できたらそこで探索終了。
  for n in reversed(range(1, N+1)):
    # 正直者の証言だけをみていく。
    tasks = combinations(list(range(N)), n)
    for honests in tasks:
      honest_set = set(honests)
      is_inconsistent = False
      for honest in honest_set:
        for i in range(N):
          # 証言の中に 「i さんは正直者」が含まれてて、正直者セットに i さんが含まれていなかった場合矛盾
          if testimony[honest][i]==1 and i not in honest_set:
            is_inconsistent = True
            break
          # 証言の中に 「i さんは不親切」が含まれてて、正直者セットに i さんが含まれていた場合矛盾
          if testimony[honest][i]==0 and i in honest_set:
            is_inconsistent = True
            break
        if is_inconsistent: break
      # 正直者全員の証言が矛盾して無かったらその時の正直者の人数が正解
      if not is_inconsistent:
        print(n)
        return

  print(0)

resolve()

if __name__ == "__main__":
    unittest.main()
