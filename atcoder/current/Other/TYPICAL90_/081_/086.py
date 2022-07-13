import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """4 2
1 2 3 50
2 3 4 45"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 2
2 3 6 1152886174205865983
1 2 8 1116611213275394047"""
        output = """395781543"""
        self.assertIO(input, output)

def resolve():
  # bit で考える。
  # Ai に関して、0 が確定する桁を考える。
  # => wi のある桁が 0 だった場合、Axi, Ayi, Azi の同じ桁は 0
  # 次に、Ai に関して、1 が確定する桁を考える。
  # => wi のある桁が 1 だった場合、Axi, Ayi, Azi の同じ桁のうち少なくとも 1 つが 1 である必要がある。
  # => Axi, Ayi, Azi の内 2 個が 0 で確定している場合、残り 1 つは 1 で確定する。
  # 各 Ai に関して、1 か 0 が確定していない桁がわかる。
  # この桁を自由に 1 or 0 に設定した場合、その組み合わせは 2**(確定していない桁の個数) になる。
  # そこから余事象を考える。
  # 各 wi の 1 になる桁の内、Axi, Ayi, Azi の同じ桁で 1 であることが確定していないものを調べる。
  # 確定していない場合、その桁が 0 になるものが余事象にあたる。
  # 
  inf = 10**18+1
  mod = 10**9+7
  bit_len = 60
  N, Q = map(int, input().split(" "))
  queries =[[int(x)-1 for x in input().split(" ")] for _ in range(Q)]

  # 桁毎に集計する。
  ws = [0]*bit_len
  for q in range(Q):
    _, _, _, w = queries[q]
    w += 1
    for j in range(bit_len):
      ws[j]+=((w>>j)&1)<<q

  # print(*queries, sep="\n")
  # print(*['{:60b}'.format(w+1) for _, _, _, w in queries], sep="\n")  
  # print(*['{:12b}'.format(w) for w in ws], sep="\n")  
  count = [0]*bit_len
  # b 桁目を見る。
  for b in range(bit_len):
    w = ws[b]
    for bit in range(2**N):
      for q in range(Q):
        x, y, z, _ = queries[q]
        if ((bit>>x&1) or (bit>>y&1) or (bit>>z&1)) != w>>q&1: break
      else:
        count[b]+=1

  # print(count)
  ans = 1
  for i in range(bit_len):
    ans *= count[i]
    if ans >= mod: ans%=mod
  print(ans)


  # ここを更新していく。
  # -1: 不定, 0: 0で確定, 1: 1 で確定
  # field = [[-1]*60 for _ in range(N)]
  # for q in range(Q):
  #   x, y, z, w = queries[q]
  #   w += 1
  #   for j in range(bit_len):
  #     if (w>>j)&1==0:
  #       field[x][j] = field[y][j] = field[z][j] = 0

  # 1 を確定する必要はあるのか・・・？
  # そもそも 0 を確定する必要もなさそう？
  # for q in range(Q):
  #   x, y, z, w = queries[q]
  #   w += 1
  #   for j in range(bit_len):
  #     if (w>>j)&1==0:
  #       field[x][j] = field[y][j] = field[z][j] = 0

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()