#include <vector>
#include <queue> 

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> minHeap(scoville.begin(), scoville.end());
    int mixCount = 0;

    // 스코빌 지수가 K 이상이 될 때까지 반복
    while (minHeap.size() > 1 && minHeap.top() < K) {
        // 가장 맵지 않은 두 개의 음식을 꺼냄
        int first = minHeap.top(); 
        minHeap.pop();
        
        int second = minHeap.top(); 
        minHeap.pop();

        // 새로운 음식의 스코빌 지수를 계산
        int newScoville = first + (second * 2);
        minHeap.push(newScoville);

        mixCount++;  // 섞은 횟수를 증가
    }

    // 모든 음식이 K 이상의 스코빌 지수를 갖는지 확인
    if (minHeap.top() < K) {
        return -1;  // 모든 음식을 섞었는데도 불가능한 경우
    }

    return mixCount;
}
