class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m];  // 경로를 저장할 DP 테이블
        
        // 물웅덩이를 0으로 설정
        for (int[] puddle : puddles) {
            int x = puddle[1] - 1;
            int y = puddle[0] - 1;
            dp[x][y] = -1;  // 물웅덩이 좌표는 -1로 표시
        }

        // 시작점
        dp[0][0] = 1;

        // DP 테이블 채우기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // 물웅덩이는 넘어감
                if (dp[i][j] == -1) {
                    dp[i][j] = 0;  // 물웅덩이이므로 경로가 없다고 표시
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

                // 나누기 연산은 모듈로 연산 (문제에서 주어진 요구사항)
                dp[i][j] %= 1000000007;
            }
        }

        // 목적지까지의 경로 수 반환
        return dp[n - 1][m - 1];
    }
}
