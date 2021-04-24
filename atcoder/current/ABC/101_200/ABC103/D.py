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
        input = """5 2
1 4
2 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9 5
1 8
2 7
3 5
4 6
7 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 例 1 だと、1 ~ 4 までの間で一本、2 ~ 5 までの間で一本の橋を落とせばいい。
  # 範囲が重なっている場合はまとめて処理できる。
  # 島じゃなくて橋で考えて、imos する？
  # 落とす橋の集合を取っていけば上手くできるか？
  # 重なっていない範囲同士に着目した方が上手くできそう。
  # A_B = [[1,10], [1, 5], [5, 20], [6, 9]] の時、[1,10] に対処するのは必須で、
  # その時に [1, 5], [5, 20] のどちらを先に対処するような切り方にするか選べる。
  # [1, 5] を同時に落とすような切断の仕方をした方が同等か良い結果になる、と仮説を立てる。
  # A_B がソートされているとすると、[1, 5], [5, 20] が重なっていない状態では、
  # それ以降に出てくる A_B 要素で [1, 5] と重なるものが出てくるのは考えられない。
  # 最初の 1 個目の A_B 要素は確実にカットする必要があるので、ans は 1 から開始する。
  # 新しく要素を取り出した時に、そこまで出てきた最大の A と最小の B の範囲で重なるか判定していって、
  # 重ならない場合に答えに +1 する。重なるなら落とす橋を追加しなくても対処可能なので答えは足さない。

  N, M = map(int, input().split(" "))
  A_B = sorted([list(map(int, input().split(" "))) for _ in range(M)])
  max_A, min_B = A_B[0]

  ans = 1
  for a, b in A_B[1:]:
    if max_A < b and a < min_B:
      max_A = max(max_A, a)
      min_B = min(min_B, b)
    else:
      max_A = a
      min_B = b
      ans += 1
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
