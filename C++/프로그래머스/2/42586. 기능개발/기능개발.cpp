#include <vector>   
#include <iostream>
 
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;           // 결과를 저장할 벡터
    vector<int> days_left;        // 각 작업이 완료되기까지 남은 일수를 저장할 벡터

    // 각 작업의 남은 일수를 계산
    for(int i = 0; i < progresses.size(); i++) {
        int remaining_days = (100 - progresses[i]) / speeds[i];
        if ((100 - progresses[i]) % speeds[i] != 0) {
            remaining_days++; // 나눗셈이 딱 떨어지지 않으면 올림처리
        }
         days_left.push_back(remaining_days); // 계산된 남은 일수를 벡터에 저장
    }

    // 배포 처리
    int first_task = days_left[0];  // 첫 번째 작업의 완료 일수
    int count = 1;                  // 첫 번째 작업을 배포하는 카운트

    for(int i = 1; i < days_left.size(); i++) {
        // 현재 작업이 첫 번째 작업과 함께 배포 가능한 경우
        if(days_left[i] <= first_task) {
            count++;  // 함께 배포할 작업 수 증가
        } else {
            // 첫 번째 작업이 완료되면 지금까지 모인 작업을 배포
            answer.push_back(count); // 배포된 작업 수 저장
            first_task = days_left[i]; // 새로운 첫 번째 작업으로 설정
            count = 1; // 카운트 초기화
        }
    }

    // 마지막 배포 처리
    answer.push_back(count);

    return answer; // 최종 결과 반환
}
