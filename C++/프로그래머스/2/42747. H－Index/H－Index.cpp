#include <vector>
#include <algorithm>  

using namespace std;

int solution(vector<int> citations) {
    // 논문 인용 횟수를 내림차순으로 정렬
    sort(citations.begin(), citations.end(), greater<int>());

    int hIndex = 0;

    // 정렬된 인용 횟수를 이용해 H-Index 계산
    for (int i = 0; i < citations.size(); i++) {
        // 현재 논문이 i번째일 때, 인용 횟수가 i+1 이상이어야 함
        if (citations[i] >= i + 1) {
            hIndex = i + 1;  // H-Index 갱신
        } else {
            break;  // 더 이상 조건을 만족하지 않으면 종료
        }
    }

    return hIndex;
}
