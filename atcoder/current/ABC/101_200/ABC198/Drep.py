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

    def test_Sample_Input_4(self):
        input = """abcd
efgh
ijkl"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """send
more
money"""
        output = """9567
1085
10652"""
        self.assertIO(input, output)

def resolve():
  from itertools import permutations

  inf = 10**18+1
  S1 = list(input())[::-1]
  S2 = list(input())[::-1]
  S3 = list(input())[::-1]
  table = set(S1+S2+S3)
  if len(table) > 10:
    print("UNSOLVABLE")
    return

  table = list(table)
  N = len(table)
  for p in permutations(range(10), N):
    dictionary = {}
    for i in range(N):
      dictionary[table[i]] = p[i]
    if dictionary[S1[-1]] == 0 or dictionary[S2[-1]] == 0 or dictionary[S3[-1]] == 0:
      continue
    s1 = 0
    for i in range(len(S1)):
      s1+=dictionary[S1[i]]*pow(10, i)
    s2 = 0
    for i in range(len(S2)):
      s2+=dictionary[S2[i]]*pow(10, i)
    s3 = 0
    for i in range(len(S3)):
      s3+=dictionary[S3[i]]*pow(10, i)
    
    if s1+s2 == s3:
      print(s1, s2, s3, sep="\n")
      return
  print("UNSOLVABLE")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()