#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int resolve(){
  int N, M;
  cin >> N >> M;

  int X0, Y0, X1, Y1, X2, Y2;
  cin >> X0 >> Y0 >> X1 >> Y1 >> X2 >> Y2;

  vector<vector<int>> TO = {{X0, Y0}, {X1, Y1}, {X2, Y2}};

  for(int i = 0; i < 3; i++){
    for(int j = 0; j < 2; j++){
      cout << TO.at(i).at(j);
      if(j < 1) cout << " ";
    }
    cout << endl;
  }

  return 0;
}

int main(){
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  return resolve();
}