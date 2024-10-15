import java.util.Stack;

class Solution {
    public int solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        // 문자열의 각 문자를 순차적으로 처리
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            // 스택이 비어 있지 않고, 스택의 top과 현재 문자가 같으면 제거
            if (!stack.isEmpty() && stack.peek() == c) {
                stack.pop();  // 스택의 top과 같은 문자 제거
            } else {
                stack.push(c);  // 같지 않으면 현재 문자를 스택에 추가
            }
        }
        
        // 스택이 비어있으면 모든 문자가 짝지어 제거된 것
        return stack.isEmpty() ? 1 : 0;
    }
}
