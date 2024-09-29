#include <vector>
#include <algorithm>  

using namespace std;

int solution(vector<int> people, int limit) {
    // 사람들의 몸무게를 오름차순으로 정렬
    sort(people.begin(), people.end());
    
    int answer = 0;  // 필요한 구명보트 수
    int left = 0;    // 가장 가벼운 사람을 가리키는 포인터
    int right = people.size() - 1;  // 가장 무거운 사람을 가리키는 포인터
    
    // 투 포인터로 사람들을 처리
    while (left <= right) {
        // 가장 가벼운 사람과 가장 무거운 사람의 무게 합이 limit 이하인 경우
        if (people[left] + people[right] <= limit) {
            left++;  // 가벼운 사람 태움
        }
        // 무거운 사람은 항상 보트에 태움
        right--;  // 무거운 사람 태움
        answer++;  // 보트 하나 사용
    }
    
    return answer;  // 총 필요한 보트 수 반환
}
