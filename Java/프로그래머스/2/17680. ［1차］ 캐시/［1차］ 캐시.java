import java.util.LinkedList;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;

        // LRU 캐시를 저장할 LinkedList 선언
        LinkedList<String> cache = new LinkedList<>();

        // 도시 이름 배열을 순회
        for (String city : cities) {
            city = city.toLowerCase();  // 모두 소문자로 변환
            
            if (cache.contains(city)) {
                answer += 1;  // 캐시 히트
                cache.remove(city);  // 기존 위치에서 도시를 제거하고
                cache.addFirst(city);  // 가장 최근 사용된 도시로 업데이트
            } else {
                answer += 5;  // 캐시 미스

                // 캐시가 꽉 찼을 경우, 가장 오래된 항목 제거
                if (cache.size() >= cacheSize && cacheSize > 0) {
                    cache.removeLast();
                }

                // 새로운 도시를 캐시의 가장 앞에 추가
                if (cacheSize > 0) {
                    cache.addFirst(city);
                }
            }
        }

        return answer;
    }
}
