import sys
pin=sys.stdin.readline
 
def comb_mod(n,r,mod):
  if n-r<r:
    r=n-r
  N=n
  R=r
  u=1
  d=1
  for i in range(r):
    u*=N
    u%=mod
    N-=1
    d*=R
    d%=mod
    R-=1
  return u*pow(d,mod-2,mod)%mod

def main():
  X,Y=map(int,pin().split())
  mod=10**9+7
  if (X+Y)%3!=0:
    print(0)
    return
  if (2*X-Y)%3!=0 or (2*Y-X)%3!=0:
    print(0)
    return
  m=(2*X-Y)//3
  n=(2*Y-X)//3
  if m<0 or n<0:
    print(0)
    return
  ans=comb_mod(m+n,min(m,n),mod)%mod
  print(ans)
  return
 
if __name__=="__main__":
  main()
