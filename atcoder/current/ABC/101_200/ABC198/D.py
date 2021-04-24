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
        input = """a
b
c"""
        output = """1
2
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """x
x
y"""
        output = """1
1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """p
q
p"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """abcd
# efgh
# ijkl"""
#         output = """UNSOLVABLE"""
#         self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """send
more
money"""
        output = """9567
1085
10652"""
        self.assertIO(input, output)

def resolve():
  # 10! = 3628800 なので、全探索で間に合いそう。
  from collections import Counter
  from itertools import permutations
  inf = 10**18+1
  S = [input() for _ in range(3)]
  all_s = "".join(S)
  c = list(Counter(all_s).keys())

  if len(c) > 10:
    print("UNSOLVABLE")
    return

  c += ["_"]*(10-len(c))
  for tar in permutations(c):
    tar = "".join(tar)
    s = [0]*3

    if tar.find(S[0][0]) == 0: continue
    if tar.find(S[1][0]) == 0: continue
    if tar.find(S[2][0]) == 0: continue

    for j in range(3):
      for i in range(len(S[j])):
        s[j] += tar.find(S[j][i])*pow(10, len(S[j]) - i - 1)
    
    # print(s)
    if s[0]+s[1] == s[2]:
       print(*s, sep="\n")
       return
  print("UNSOLVABLE")
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
