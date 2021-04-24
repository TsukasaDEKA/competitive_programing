# 繰り返し二乗法
# n**x
# python の組み込み関数 pow では内部的にこれをやってるので、使うことはなさそう。
import sys
sys.setrecursionlimit(500*500)

def repeat_squaring(n, p, mod=None):
  if p==0: return 1
  if p%2==0:
    temp = repeat_squaring(n, p//2, mod)**2
    if mod is not None: temp%=mod
    return temp
  return n*repeat_squaring(n, p-1, mod)

print(repeat_squaring(2, 36))
