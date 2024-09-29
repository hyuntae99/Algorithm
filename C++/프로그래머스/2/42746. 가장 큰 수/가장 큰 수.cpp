#include <string>
#include <vector>
#include <algorithm>  

using namespace std;

// 문자열을 결합하여 두 숫자를 비교하는 함수
bool compare(string a, string b) {
    return a + b > b + a;  // 두 문자열을 합친 결과를 비교하여 큰 쪽이 먼저 오도록 정렬
}

string solution(vector<int> numbers) {
    vector<string> str_numbers; 

    // 각 숫자를 문자열로 변환
    for (int num : numbers) {
        str_numbers.push_back(to_string(num));
    }

    // 사용자 정의 비교 함수를 이용해 정렬
    sort(str_numbers.begin(), str_numbers.end(), compare);

    // 모든 숫자가 0일 경우 "0"을 반환
    if (str_numbers[0] == "0") {
        return "0";
    }

    // 정렬된 문자열을 이어 붙여 결과 반환
    string answer = "";
    for (string num : str_numbers) {
        answer += num;
    }

    return answer;
}
