#include <iostream>

using namespace std;

int main() 
{
    
    int N,M;
    int s = 0;
    int e = 1;
    int ans = 0;
    
    cin >> N >> M;

    int A[N+1];
    
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    int tmp = A[0];
    
    while(e<N){
        if(tmp + A[e] <= M){
            tmp += A[e];
            e+=1;
            ans = max(tmp,ans);
        }
        else{
            tmp -= A[s];
            s+=1;

        }

    }
    
    
    cout << ans << '\n';
    
    return 0;
}
