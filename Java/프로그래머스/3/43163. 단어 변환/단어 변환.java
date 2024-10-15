import java.util.*;

class Solution {
    static int[] v;
    
    public int solution(String begin, String target, String[] words) {
        
        return bfs(begin, target, words);
    }
    
    // 두 단어의 차이가 1개인지 확인하는 함수
    public boolean find(String word1, String word2) {
        int cnt = 0;
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                cnt++;
            }
            if (cnt > 1) {
                return false;
            }
        }
        return true;
    }
    
    public int bfs(String begin, String target, String[] words) {
        int len = words.length;
        Queue<String> q = new LinkedList<>();
        v = new int[len]; // 방문 체크 배열
        
        q.offer(begin);
        int steps = 0; // 단어 변환 횟수
        
        while (!q.isEmpty()) {
            int qSize = q.size(); // 한 레벨에서 탐색할 단어 수
            steps++;
            
            for (int i = 0; i < qSize; i++) {
                String current = q.poll();
                
                for (int j = 0; j < len; j++) {
                    if (v[j] == 0 && find(current, words[j])) {
                        if (words[j].equals(target)) {
                            return steps;
                        }
                        v[j] = 1; // 방문 체크
                        q.offer(words[j]); // 다음 단어 큐에 삽입
                    }
                }
            }
        }
        
        return 0; // 타겟 단어에 도달할 수 없는 경우
    }
}
