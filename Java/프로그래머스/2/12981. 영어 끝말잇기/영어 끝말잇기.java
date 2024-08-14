import java.util.HashSet;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        HashSet<String> usedWords = new HashSet<>(); // 사용된 단어를 저장할 집합
        
        int cnt = 1; // 사람 번호
        boolean isSuccess = true;

        for (int i = 0; i < words.length; i++) {
            // 사람 번호를 넘어가면 
            if (cnt > n) {
                cnt = 1;
            }
            
            // 끝말잇기에 실패하거나 같은 단어를 말했을 경우
            if ((i > 0 && words[i].charAt(0) != words[i-1].charAt(words[i-1].length() - 1)) 
                || usedWords.contains(words[i])) {
                
                answer[0] = cnt;  // 현재 사람 번호 저장
                answer[1] = (i / n) + 1;  // 현재 사람의 턴 계산
                isSuccess = false;
                break;
            }
            
            // 사용된 단어로 추가
            usedWords.add(words[i]);
            cnt += 1;
        }

        // 성공했다면
        if (isSuccess) {
            answer[0] = 0;
            answer[1] = 0;
        }
        
        return answer;
    }
}
