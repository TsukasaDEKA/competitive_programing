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

#     def test_Sample_Input_1(self):
#         input = """3
# 011"""
#         output = """2
# 1
# 1"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """23
00110111001011011001110"""
        output = """2
1
2
2
1
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
1
3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
00000000"""
        output = """1
1
1
1
1
1
1
1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
0"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """2
10"""
        output = """0
2"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  X = input()

  if N == 1:
    if X.count("1"):
      print(0)
    else:
      print(1)
    return True

  base_1_count = X.count("1")
  if base_1_count == 0:
    for _ in range(N):
      print(1)
    return True

  X_int = int(X, 2)
  X_int_p = X_int%(base_1_count + 1)

  # RE 対策
  if base_1_count == 1:
    for i in range(N):
      if X[i] == "1":
        print(0)
      else:
        if i == N - 1:
          Xi = X_int_p + 1
        else:
          Xi = X_int_p
        count = 1
        while Xi != 0:
          Xi %= bin(Xi).count("1")
          count += 1
        print(count)
    return True

  X_int_m = X_int%(base_1_count - 1)
  for i in range(N):
    # 初期値計算を高速にやる
    if X[i] == "1":
      temp_1_count = base_1_count-1
      pow_2 = pow(2, N-i-1, base_1_count-1)
      if X_int_m <= pow_2:
        Xi = X_int_m - pow_2 + base_1_count-1
      else:
        Xi = X_int_m - pow_2
    else:
      temp_1_count = base_1_count+1
      Xi = X_int_p + pow(2, N-i-1, base_1_count+1)
      while Xi >= base_1_count+1:
        Xi %= base_1_count+1

    # print("1_c={0}".format(temp_1_count))
    if temp_1_count == Xi:
      print(1)
      continue

    count = 1
    while Xi != 0:
      num_of_1 = bin(Xi).count("1")
      Xi %= num_of_1
      count += 1
    print(count)

# if __name__ == "__main__":
#     resolve()

if __name__ == "__main__":
    unittest.main()
