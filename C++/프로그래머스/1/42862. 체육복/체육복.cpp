#include <vector>
#include <algorithm>  // sort를 사용하기 위한 헤더

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    // 우선 lost와 reserve를 정렬
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());

    // 중복된 학생을 처리: 여벌이 있는 학생이 도난당한 경우 제거
    vector<int>::iterator it;
    for (int i = 0; i < lost.size(); i++) {
        it = find(reserve.begin(), reserve.end(), lost[i]);
        if (it != reserve.end()) {
            reserve.erase(it);  // reserve에서 제거
            lost.erase(lost.begin() + i);  // lost에서도 제거
            i--;  // 인덱스를 유지하기 위해 i 감소
        }
    }

    // 체육 수업에 참여할 수 있는 학생 수를 n - 실제로 잃어버린 학생 수로 시작
    int answer = n - lost.size();

    // 여벌 체육복을 빌려주는 과정
    for (int i = 0; i < lost.size(); i++) {
        for (int j = 0; j < reserve.size(); j++) {
            if (reserve[j] == lost[i] - 1 || reserve[j] == lost[i] + 1) {
                answer++;  // 체육복을 빌려주면 체육 수업에 참여 가능
                reserve.erase(reserve.begin() + j);  // 빌려준 학생은 reserve에서 제거
                break;
            }
        }
    }

    return answer; 
}
