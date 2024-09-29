#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

int solution(int N, int number) {
    // 1부터 8까지의 숫자 사용 횟수에 따라 만들 수 있는 숫자를 저장하는 벡터
    vector<set<int>> dp(9);  // dp[1]은 N을 1번 사용해서 만들 수 있는 숫자들
    
    // N을 i번 반복해서 만든 숫자를 넣어줌 (N, NN, NNN, ...)
    for (int i = 1; i <= 8; i++) {
        dp[i].insert(stoi(string(i, '0' + N)));
    }
    
    // 1부터 8번까지 N을 사용하여 만들 수 있는 모든 경우를 계산
    for (int i = 1; i <= 8; i++) {
        for (int j = 1; j < i; j++) {
            for (int a : dp[j]) {
                for (int b : dp[i - j]) {
                    // 사칙연산을 사용하여 숫자를 만듦
                    dp[i].insert(a + b);
                    dp[i].insert(a - b);
                    dp[i].insert(a * b);
                    if (b != 0) dp[i].insert(a / b);
                }
            }
        }
        
        // 현재 계산한 숫자들 중에서 number가 있는지 확인
        if (dp[i].count(number)) {
            return i;  // number를 만들 수 있는 최소 사용 횟수 반환
        }
    }
    
    return -1;  // 8번 이하로 만들 수 없으면 -1 반환
}
