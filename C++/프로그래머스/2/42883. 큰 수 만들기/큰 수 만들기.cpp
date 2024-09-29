#include <string>
#include <stack>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    
    for (int i = 0; i < number.size(); i++) {
        // 제거할 숫자가 남아있고, 현재 숫자가 앞에 있는 숫자보다 크면 앞의 숫자를 제거
        while ((!answer.empty()) && (k > 0) && (answer.back() < number[i])) {
            answer.pop_back();
            k--;  // 제거할 숫자 감소
        }
        
        // 결과에 숫자 추가
        answer.push_back(number[i]);
    }
    
    // 만약 k가 남아있는 경우, 뒤에서부터 k개를 자름
    if (k > 0) {
        answer = answer.substr(0, answer.size() - k);
    }

    return answer;
}
