#include <vector>       
#include <queue>       
#include <algorithm>   

using namespace std;

// 프린터 인쇄 순서를 계산하는 함수
int solution(vector<int> priorities, int location) {
    queue<pair<int, int>> printerQueue;  // (문서의 중요도, 문서의 위치)를 저장하는 큐
    int answer = 0;                      // 인쇄 순서를 저장하는 변수

    // 우선순위 큐에 문서 삽입
    for(int i = 0; i < priorities.size(); i++) {
        printerQueue.push({priorities[i], i}); // 중요도와 위치를 큐에 저장
    }

    // 인쇄 작업 시작
    while(!printerQueue.empty()) {
        // 현재 큐에서 가장 앞에 있는 문서
        int current_priority = printerQueue.front().first;
        int current_location = printerQueue.front().second;
        printerQueue.pop();

        // 현재 문서보다 더 높은 중요도를 가진 문서가 있는지 확인
        bool has_higher_priority = false;
        for(int i = 0; i < priorities.size(); i++) {
            if (priorities[i] > current_priority) {
                has_higher_priority = true;
                break;
            }
        }

        // 더 높은 중요도를 가진 문서가 있는 경우, 다시 큐의 뒤로 보냄
        if (has_higher_priority) {
            printerQueue.push({current_priority, current_location});
        } else {
            // 더 높은 중요도를 가진 문서가 없으면, 인쇄
            answer++;  // 인쇄 순서 증가
            priorities[current_location] = 0;  // 인쇄된 문서의 중요도를 0으로 변경

            // 인쇄한 문서가 우리가 찾고 있는 문서인 경우
            if (current_location == location) {
                return answer;  // 몇 번째로 인쇄되었는지 반환
            }
        }
    }

    return answer;
}
