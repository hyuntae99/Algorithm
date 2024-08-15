import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        // 문자열을 소문자로 변환한 후 다중집합으로 변환
        List<String> multiset1 = makeMultiset(str1.toLowerCase());
        List<String> multiset2 = makeMultiset(str2.toLowerCase());
        
        // 교집합과 합집합의 크기를 구하기 위한 맵 생성
        Map<String, Integer> map1 = getCountMap(multiset1);
        Map<String, Integer> map2 = getCountMap(multiset2);
        
        // 교집합 크기 계산
        int intersectionSize = 0;
        for (String key : map1.keySet()) {
            if (map2.containsKey(key)) {
                // 공통된 원소의 경우, 최소 등장 횟수만큼 교집합에 추가
                intersectionSize += Math.min(map1.get(key), map2.get(key));
            }
        }
        
        // 합집합 크기 계산
        int unionSize = 0;
        Set<String> allKeys = new HashSet<>();
        allKeys.addAll(map1.keySet());
        allKeys.addAll(map2.keySet());
        
        for (String key : allKeys) {
            int count1 = map1.getOrDefault(key, 0);
            int count2 = map2.getOrDefault(key, 0);
            // 공통된 원소는 최대 등장 횟수만큼, 아닌 원소는 각자 등장 횟수만큼 합집합에 추가
            unionSize += Math.max(count1, count2);
        }
        
        // 자카드 유사도 계산
        double jaccardSimilarity = (unionSize == 0) ? 1.0 : (double) intersectionSize / (double) unionSize;
        
        // 자카드 유사도에 65536을 곱한 후 정수로 반환
        return (int) (jaccardSimilarity * 65536);
    }
    
    // 두 글자씩 끊어서 다중집합을 만드는 함수
    private List<String> makeMultiset(String str) {
        List<String> multiset = new ArrayList<>();
        
        for (int i = 0; i < str.length() - 1; i++) {
            char first = str.charAt(i);
            char second = str.charAt(i + 1);
            
            if (Character.isLetter(first) && Character.isLetter(second)) {
                multiset.add("" + first + second);
            }
        }
        return multiset;
    }
    
    // 리스트에서 각 원소의 등장 횟수를 세는 함수
    private Map<String, Integer> getCountMap(List<String> multiset) {
        Map<String, Integer> countMap = new HashMap<>();
        
        for (String s : multiset) {
            countMap.put(s, countMap.getOrDefault(s, 0) + 1);
        }
        
        return countMap;
    }
}
