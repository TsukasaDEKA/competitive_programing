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

    def test_sample1(self):
        input = """3 10
15 11
10 6
6 4"""
        output = """16"""
        self.assertIO(input, output)

#     def test_sample2(self):
#         input = """30 499887702
# 128990795 137274936
# 575374246 989051853
# 471048785 85168425
# 640066776 856699603
# 819841327 611065509
# 704171581 22345022
# 536108301 678298936
# 119980848 616908153
# 117241527 28801762
# 325850062 478675378
# 623319578 706900574
# 998395208 738510039
# 475707585 135746508
# 863910036 599020879
# 340559411 738084616
# 122579234 545330137
# 696368935 86797589
# 665665204 592749599
# 958833732 401229830
# 371084424 523386474
# 463433600 5310725
# 210508742 907821957
# 685281136 565237085
# 619500108 730556272
# 88215377 310581512
# 558193168 136966252
# 475268130 132739489
# 303022740 12425915
# 122379996 137199296
# 304092766 23505143"""
#         output = """3673016420"""
#         self.assertIO(input, output)

    def test_sample3(self):
        input = """10 2921
981421680 325
515936168 845
17309336 371
788067075 112
104855562 96
494541604 960
32007355 161
772339969 581
55112800 248
98577050 22"""
        output = """3657162058"""
        self.assertIO(input, output)

#     def test_sample4(self):
#         input = """10 936447862
# 854 810169801
# 691 957981784
# 294 687140254
# 333 932608409
# 832 42367415
# 642 727293784
# 139 870916042
# 101 685539955
# 853 243593312
# 369 977358410"""
#         output = """1686"""
#         self.assertIO(input, output)


def resolve():
  N, W = map(int, input().split(" "))

  dp = [[0]*(W+1) for _ in range(N+1)]

  for i in range(1, N+1):
    v, w = map(int, input().split(" "))
    if w < W:
      dp[i][:w] = dp[i-1][:w]
      for j in range(w, W+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    else:
      dp[i][:] = dp[i-1][:]

  print(max(dp[N]))

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
