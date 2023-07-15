#include <iostream>

using namespace std;

int main() {
  int n, m;
  cin >> n >> m;

  int ingots[100];
  for(int i = 0; i < n; ++i){
    cin >> ingots[i];
  }

  int bag[100][10000];
  for(int i = 0; i < n + 1; ++i){
    for(int j = 0; j < m + 1; ++j){
      bag[i][j] = 0;
    }
  }

  for(int i = 1; i < n + 1; ++i){
    for(int j = 1; j < m + 1; ++j){
      if(ingots[i - 1] > j){
        bag[i][j] = bag[i - 1][j];
      } else {
        bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - ingots[i - 1]] + ingots[i - 1]);
      }
    }
  }

  cout << bag[n][m] << endl;
  return 0;
}