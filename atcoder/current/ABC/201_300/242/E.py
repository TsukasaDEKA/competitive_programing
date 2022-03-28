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
        input = """5
3
AXA
6
ABCZAZ
30
QWERTYUIOPASDFGHJKLZXCVBNMQWER
28
JVIISNEOXHSNEAAENSHXOENSIIVJ
31
KVOHEEMSOZZASHENDIGOJRTJVMVSDWW"""
        output = """24
29
212370247
36523399
231364016"""
        self.assertIO(input, output)

def resolve():
  alpha2num = lambda c: ord(c) - ord('A')

  mod = 998244353
  inf = 10**18+1
  # 前から決めていける。
  # i 番目の文字と N-i 番目の文字は一緒
  # S[i] <= S[N-i] の時、特に気にする必要はない。
  # S[i] > S[N-i] の時、それ以降の or 以前のどこかで辞書順で小さくなる必要がある。
  # X[i] < S[i] の時、他の文字は回文であれば自由に選べる。
  # 
  T = int(input())
  for _ in range(T):
    N = int(input())
    S = [alpha2num(x) for x in list(input())]
    # N = (len(S)+1)//2
    ans = 1
    for i in range((N+1)//2):
      if S[i] <= S[N-1-i]:
        ans+=S[i]*pow(26, (N+1)//2-i-1)
      else:
        ans+=
      if ans >= mod: ans %= mod
    print(ans)

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()