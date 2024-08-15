import java.util.HashMap;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        // 원할 때의 물건과 수량을 저장할 HashMap 생성
        HashMap<String, Integer> wantMap = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], number[i]);
        }
        
        // 10일씩 확인하면서 진행
        for (int i = 0; i <= discount.length - 10; i++) {
            // 현재 10일 간의 구간에서 물건의 수량을 체크할 HashMap
            HashMap<String, Integer> currentMap = new HashMap<>();
            
            // 해당 구간의 할인 항목을 currentMap에 저장
            for (int j = i; j < i + 10; j++) {
                currentMap.put(discount[j], currentMap.getOrDefault(discount[j], 0) + 1);
            }
            
            // 원하는 항목들이 모두 조건을 만족하는지 확인
            boolean isMatch = true;
            for (String item : wantMap.keySet()) {
                if (currentMap.getOrDefault(item, 0) < wantMap.get(item)) {
                    isMatch = false;
                    break;
                }
            }
            
            // 모든 조건이 맞으면 answer 증가
            if (isMatch) {
                answer++;
            }
        }

        return answer;
    }
}
