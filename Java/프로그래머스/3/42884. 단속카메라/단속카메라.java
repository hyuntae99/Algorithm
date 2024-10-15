import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;

        // 나가는 지점이 작은 순으로 정렬
        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));

        // 첫 번째 차량의 나가는 지점에 카메라를 설치
        int cam = routes[0][1]; 
        answer++;  // 첫 번째 카메라 설치

        for (int i = 1; i < routes.length; i++) {
            // 카메라가 다음 차량의 진입 지점을 커버하지 못하는 경우
            if (cam < routes[i][0]) {
                answer++;  // 새로운 카메라 설치
                cam = routes[i][1];  // 새로운 카메라의 위치
            }
        }

        return answer;
    }
}
