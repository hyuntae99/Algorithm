class Solution {
    boolean solution(String s) {
        int cnt = 0;  // 여는 괄호와 닫는 괄호의 균형을 맞추기 위한 변수

        for (int i = 0; i < s.length(); i++) {
            // 여는 괄호면 증가
            if (s.charAt(i) == '(') {
                cnt++;
            } 
            // 닫는 괄호면 감소
            else {
                cnt--;
            }
            
            // 만약 중간에 닫는 괄호가 먼저 나온 경우 (cnt가 음수가 되면) 바로 false 반환
            if (cnt < 0) {
                return false;
            }
        }
        
        // 모든 문자를 확인 후 여는 괄호와 닫는 괄호의 수가 같으면 true, 아니면 false
        return cnt == 0;
    }
}
