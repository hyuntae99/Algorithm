#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 참가자 중 완주하지 못한 선수를 찾는 함수
string solution(vector<string> participant, vector<string> completion) {
    string answer = ""; // 최종 답변을 저장할 변수 초기화

    // 참가자 목록과 완주자 목록을 정렬
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    // 완주자 목록의 크기만큼 반복하면서 참가자와 완주자를 비교
    for (int i = 0; i < completion.size(); i++) {
        // 만약 참가자[i]와 완주자[i]가 다르다면, 해당 참가자가 미완주자
        if (participant[i] != completion[i]) {
            answer = participant[i]; // 미완주자 이름을 저장
            break; // 반복문 종료
        }
    }

    // 모든 참가자가 완주자와 일치했다면, 마지막 참가자가 미완주자
    if (answer == "") {
        answer = participant.back(); // 마지막 참가자 이름을 저장
    }

    return answer; // 미완주자 이름 반환
}
