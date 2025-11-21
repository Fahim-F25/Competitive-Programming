#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
    bool checkIfPangram(string sentence) {
        bool allFind = true;
     for(char c = 'a'; c <= 'z'; c++){
        if(sentence.find(c) == string :: npos){
            allFind = false;
            break;
        }   
        }
        if(allFind == true)
        {
            return true;
        }
        else{
            return false;
        }
     }   
    };
int main() {
    Solution sol;
    string sentence;
    cin >> sentence;
    if(sol.checkIfPangram(sentence) == true){
        cout << "true" << endl;
    }
    else{
        cout << "false" << endl;
    }
    return 0;
}