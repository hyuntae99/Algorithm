import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        // 귤 크기별 빈도를 저장할 HashMap
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // 귤 크기별로 빈도 계산 -> 값이 존재하지않으면 0으로 간주
        for (int i = 0; i < tangerine.length; i++) {
            map.put(tangerine[i], map.getOrDefault(tangerine[i], 0) + 1);
        }
        
        // 빈도를 기준으로 내림차순 정렬
        List<Integer> frequencies = new ArrayList<>(map.values());
        frequencies.sort(Collections.reverseOrder());

        
        // 목표 k만큼의 귤을 채울 때까지 빈도가 큰 순서대로 귤을 고른다
        int total = 0;
        for (int frequency : frequencies) {
            total += frequency;
            answer++;
            if (total >= k) {
                break;
            }
        }
        
        return answer;
    }
}
