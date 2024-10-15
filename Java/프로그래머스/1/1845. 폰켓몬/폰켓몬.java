import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {                
        int n = nums.length / 2;  // 배열의 크기의 절반을 계산
       
        // 배열에서 중복을 제거한 Set을 생성
        Set<Integer> num_set = new HashSet<>();
        for (int num : nums) {
            num_set.add(num);
        }
        
        // Set의 크기와 n 중 작은 값을 선택
        int answer = Math.min(n, num_set.size());
        
        return answer;
    }
}
