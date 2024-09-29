#include <string>  

using namespace std;

bool solution(string s) {
    int count = 0;

    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '(') {
            count++;  // 열린 괄호를 만나면 카운트 증가
        } else {
            count--;  // 닫힌 괄호를 만나면 카운트 감소
        }

        // 만약 카운트가 음수가 되면 올바르지 않은 괄호
        if(count < 0) {
            return false;  
        }
    }

    bool answer = true;
    if (count != 0) {
        answer = false;
    }
    return answer;
}
