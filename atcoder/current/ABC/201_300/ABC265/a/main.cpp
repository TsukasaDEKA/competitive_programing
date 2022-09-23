#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int resolve(){
  int X, Y, N;
  cin >> X >> Y >> N;

  int ans = min(N*X, (N/3)*Y + (N%3)*X);
  cout << ans << "\n";

  return 0;
}

int main(){
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  return resolve();
}