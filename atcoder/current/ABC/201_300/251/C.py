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
        input = """3
aaa 10
bbb 20
aaa 30"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
aaa 9
bbb 10
ccc 10
ddd 10
bbb 11"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
bb 3
ba 1
aa 4
bb 1
ba 5
aa 9
aa 2
ab 6
bb 5
ab 3"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  temp = set()
  ans = 0
  point = -1
  for i in range(N):
    S, T = [x for x in input().split(" ")]
    T = int(T)
    if S in temp: continue
    temp.add(S)
    
    if T > point:
      ans = i+1
      point = T
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()