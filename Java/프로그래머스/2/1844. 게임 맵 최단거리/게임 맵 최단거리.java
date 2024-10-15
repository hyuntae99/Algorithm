import java.util.*;

class Solution {
    // 북, 남, 서, 동 방향 정의
    int[] ddi = {-1, 1, 0, 0};  // 행 방향 이동
    int[] ddj = {0, 0, -1, 1};  // 열 방향 이동
    
    public int bfs(int si, int sj, int ei, int ej, int[][] maps) {
        // BFS를 위한 큐 선언 (LinkedList로 구현)
        Queue<int[]> q = new LinkedList<>();
        int[][] v = new int[ei+1][ej+1];  // 방문 배열 초기화
        v[si][sj] = 1;  // 시작점 방문 표시
        q.offer(new int[] {si, sj});  // 큐에 시작점 추가

        // BFS 실행
        while (!q.isEmpty()) {
            int[] current = q.poll();  // 현재 좌표
            int ci = current[0];  // 현재 위치의 행
            int cj = current[1];  // 현재 위치의 열
            
            // 목적지에 도착하면 현재까지 이동한 거리 반환
            if (ci == ei && cj == ej) {
                return v[ci][cj];
            }
            
            // 네 방향으로 이동
            for (int i = 0; i < 4; i++) {
                int ni = ci + ddi[i];
                int nj = cj + ddj[i];
                
                // 범위 내 + 길 + 방문x
                if (ni >= 0 && ni <= ei && nj >= 0 && nj <= ej && maps[ni][nj] == 1 && v[ni][nj] == 0) {
                    q.offer(new int[] {ni, nj});  // 새로운 좌표를 큐에 추가
                    v[ni][nj] = v[ci][cj] + 1;  // 이동한 거리를 기록
                }
            }
        }

        return -1;  // 도착할 수 없는 경우 -1 반환
    }
    
    public int solution(int[][] maps) {
        // BFS를 실행하여 최단 경로 반환
        int answer = bfs(0, 0, maps.length-1, maps[0].length-1, maps);
        
        return answer;
    }
}
