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
        input = """0 8 1 3 5 4 9 7 6 2
10
1
2
3
4
5
6
7
8
9
10"""
        output = """8
1
3
5
4
9
7
6
2
10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 9 8 7 6 5 4 3 2 1
3
13467932
98738462
74392"""
        output = """74392
98738462
13467932"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 1 2 3 4 5 6 7 8 9
4
643
1234
43
909"""
        output = """43
643
909
1234"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """0 7 4 3 9 5 6 2 1 8
2
333
333"""
        output = """333
333"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """0 2 4 6 8 1 3 5 7 9
1
10"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  # 置き換えてソート
  B = [int(x) for x in input().split(" ")]
  mapedB = [0]*10
  for i in range(10):
    mapedB[B[i]] = str(i)
  del B
  N = int(input())

  ans = []
  for _ in range(N):
    tar = int(input())
    conv = [0]*len(str(tar))
    for i in range(len(conv)):
      conv[i] = mapedB[(tar//(10**i))%10]
    ans.append((tar, int("".join(reversed(conv)))))
    del tar, conv
  ans.sort(key=lambda x: x[1])

  for a, _ in ans:
    print(a)

resolve()

if __name__ == "__main__":
    unittest.main()
