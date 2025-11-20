#include<iostream>
using namespace std;

int mulDiv(int num)
{
    int movesNeed = 0;
    while (num != 1)
    {
        if (num % 6 == 0){
            num = num / 6;
        }
        else{
            num = num * 2;
        }

        if (num > 1e9){
            return -1;
        }
        movesNeed = movesNeed + 1;
    }
    return movesNeed;
    
}

int main()
{
    int t,n;

    cin >> t;
    for(int i = 0; i<t; i++){
        cin >> n;
        cout << mulDiv(n) << endl;
    }
    return 0;
}