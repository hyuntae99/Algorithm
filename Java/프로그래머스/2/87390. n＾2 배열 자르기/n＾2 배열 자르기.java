import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Long> solution(int n, long left, long right) {
        List<Long> result = new ArrayList<>();
        
        for (long i = left; i <= right; i++) {
            long row = i / n;
            long col = i % n;
            result.add(Math.max(row + 1, col + 1));
        }
        
        return result;
    }
}
