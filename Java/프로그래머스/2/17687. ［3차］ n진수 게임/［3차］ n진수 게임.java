import java.util.ArrayList;

public class Solution {
    // n진법으로 숫자를 변환하는 메서드
    public static String convertToBaseN(int num, int base) {
        String chars = "0123456789ABCDEF"; 
        StringBuilder result = new StringBuilder(); 
        
        // 0일 경우에도 처리 필요
        if (num == 0) {
            return "0";
        }

        while (num > 0) {
            result.append(chars.charAt(num % base)); 
            num /= base; 
        }

        // 숫자가 뒤집혀 있으므로 반전하여 반환
        return result.reverse().toString();
    }

    public String solution(int n, int t, int m, int p) {
        StringBuilder gameSequence = new StringBuilder();  
        int number = 0;
        
        // t * m 이상의 문자가 나올 때까지 반복
        while (gameSequence.length() < t * m) {
            // 진법 변환
            gameSequence.append(convertToBaseN(number++, n));  
        }
        
        StringBuilder answer = new StringBuilder(); 
        
        // 튜브가 말할 문자를 순서에 맞게 추출
        for (int i = 0; i < t; i++) {
            answer.append(gameSequence.charAt(i * m + p - 1));  
        }
        
        return answer.toString(); 
    }
}
