#include <vector>

using namespace std;

int dfs(const vector<int>& numbers, int target, int index, int currentSum) {
    // 모든 숫자를 다 사용한 경우
    if (index == numbers.size()) {
        // 타겟 넘버와 현재 합계가 같으면 1, 아니면 0 반환
        return (currentSum == target) ? 1 : 0;
    }

    // 현재 숫자를 더하거나 빼는 두 가지 경우로 재귀 호출
    return dfs(numbers, target, index + 1, currentSum + numbers[index]) +
           dfs(numbers, target, index + 1, currentSum - numbers[index]);
}

int solution(vector<int> numbers, int target) {
    return dfs(numbers, target, 0, 0);  // DFS 탐색 시작
}
