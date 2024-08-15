import java.util.*;

class Solution {
    public int solution(int[] elements) {
        HashSet<Integer> nums = new HashSet<>(); // 계산된 수열 저장
        
        nums.add(Arrays.stream(elements).sum()); // 모든 값을 더한 수열 저장
        
        // 간격 별로 연속 부분 수열 계산
        for (int gap = 1; gap < elements.length; gap++) {
            // 배열의 크기만큼 반복
            for (int i = 0; i < elements.length; i++) {
                int num = 0;
                for (int j = 0; j < gap; j++) {
                    num += elements[(i + j) % elements.length];
                }
                nums.add(num);
            }
        }
        
        return nums.size();
    }
}