#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    vector<vector<int>> dp(n, vector<int>(m, 0));  // DP 테이블 초기화
    
    // 물웅덩이는 -1로 설정
    for (const auto& puddle : puddles) {
        dp[puddle[1] - 1][puddle[0] - 1] = -1;
    }
    
    // 시작점 초기화
    dp[0][0] = 1;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (dp[i][j] == -1) {  // 물웅덩이일 경우 처리
                dp[i][j] = 0;
                continue;
            }
            // 위쪽에서 오는 경로
            if (i > 0) {
                dp[i][j] += dp[i - 1][j];
            }
            // 왼쪽에서 오는 경로
            if (j > 0) {
                dp[i][j] += dp[i][j - 1];
            }
            dp[i][j] %= 1000000007;  // 문제에서 요구한 모듈러 연산
        }
    }
    
    return dp[n - 1][m - 1];  // 도착점까지의 경로 개수 반환
}
