#include <iostream>
using namespace std;

int main() {
    int N = 0;
    cin >> N;
    int lst[50][2] = {0};
    int ans[50] = {0};

    for (int i = 0; i < N ; i++){
        cin >> lst[i][0] >> lst[i][1];
        ans[i] = 1;
    }

    for (int i = 0 ; i < N ; i++){
        for (int j = 0 ; j < N ; j++){
            if (lst[i][0] < lst[j][0] && lst[i][1] < lst[j][1]) {
                ans[i] ++;
            }
        }
    }

    for (int i = 0; i < N; i++){
        cout << ans[i] << " ";
    }

    return 0;

}