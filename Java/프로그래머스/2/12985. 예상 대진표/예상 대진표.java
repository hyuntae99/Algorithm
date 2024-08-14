class Solution {
    public int solution(int n, int a, int b) {
        int answer = 0; 
        
        while (a != b) {
            // A와 B의 다음 라운드 번호 계산
            a = (a + 1) / 2;
            b = (b + 1) / 2;
            answer++; // 라운드 증가
        }

        return answer;
    }
}
