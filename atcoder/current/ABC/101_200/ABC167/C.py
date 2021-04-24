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
        input = """3 3 10
60 2 2 4
70 8 7 9
50 2 3 9"""
        output = """120"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """3 3 10
100 3 1 4
100 1 5 9
100 2 6 5"""
        output = """-1"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """8 5 22
100 3 7 5 3 1
164 4 5 2 7 8
334 7 2 7 2 9
234 4 7 2 8 2
541 5 4 3 3 6
235 4 8 6 9 7
394 3 6 1 6 2
872 8 4 3 7 2"""
        output = """1067"""
        self.assertIO(input, output)
    def test_Sample_Input_4(self):
        input = """1 3 10
60 0 0 0"""
        output = """-1"""
        self.assertIO(input, output)
    def test_Sample_Input_5(self):
        input = """1 3 10
60 10 10 10"""
        output = """60"""
        self.assertIO(input, output)

from itertools import product
from itertools import combinations
import numpy as np

def resolve():
  N, M, X = map(int, input().split(" "))

  books = []
  for i in range(N):
    CA = [int(x) for x in input().split(" ")]
    books.append(CA)

  books = np.array(books)


  if N == 1:
    if np.all(books[:, 1:] >= X):
      print(books[0][0])
    else:
      print(-1)
    return True
  books_index_pattarns = [list(x) for i in range(1, N+1) for x in combinations(range(0, N), i)]
  books_result = np.array([np.sum(books[x], axis=0) for x in books_index_pattarns])
  books_result = books_result[np.all(books_result[:,1:] >= X, axis=1)]

  if len(books_result) == 0:
    print(-1)
    return True
  elif len(books_result) == 1:
    print(books_result[0][0])
    return True
  else:
    # print(books_result)
    print(books_result[:,:1].min())
    return True

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()