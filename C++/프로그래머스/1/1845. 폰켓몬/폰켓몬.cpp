#include <vector>   
#include <algorithm> 
#include <unordered_set> 

using namespace std;

// 폰켓몬 종류를 선택하는 최대 종류 수를 반환하는 함수
int solution(vector<int> nums) {
    // 1. 중복을 제거하기 위해 unordered_set을 사용하여 고유한 폰켓몬 종류를 저장
    unordered_set<int> unique_poketmons(nums.begin(), nums.end());

    // 2. 선택할 수 있는 폰켓몬의 수는 전체 폰켓몬 수의 절반
    int max_select = nums.size() / 2;

    // 3. 최대 종류 수는 선택 가능한 수와 고유한 폰켓몬 수 중 작은 값
    return min(max_select, (int)unique_poketmons.size());
}
