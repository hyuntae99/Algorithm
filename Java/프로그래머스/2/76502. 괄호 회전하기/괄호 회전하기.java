import java.util.Stack;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        // 왼쪽으로 몇 칸 이동할 것인가
        for (int i = 0; i < s.length(); i++) {
            // 왼쪽으로 이동시킨 문자열을 뒤에 연결
            String newString = s.substring(i, s.length()) + s.substring(0, i);
            // 문자열이 올바른지 확인하는 함수 이용
            if (isRight(newString)) {
                answer++;
            }
        }
        
        return answer;
    }
    
    public boolean isRight(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            // 여는 괄호는 스택에 넣는다
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else {
                // 닫는 괄호인데 스택이 비어있으면 올바르지 않음
                if (stack.isEmpty()) {
                    return false;
                }
                
                // 스택의 맨 위 값이 대응하는 여는 괄호인지 확인
                char top = stack.pop();
                if ((ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '[')) {
                    return false;
                }
            }
        }
        
        // 모든 괄호가 짝을 맞췄는지 확인
        return stack.isEmpty();
    }
}
