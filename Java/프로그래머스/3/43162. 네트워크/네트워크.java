import java.util.*;

class Solution {
    int[] v;  // 방문 여부를 저장할 배열

    public void bfs(int s, int[][] computers, int n) {
        Queue<Integer> q = new LinkedList<>();
        v[s] = 1;  // 시작 컴퓨터 방문 표시
        q.offer(s);  // 큐에 시작점 추가

        while (!q.isEmpty()) {
            int c = q.poll();  // 현재 컴퓨터

            // 현재 컴퓨터와 연결된 다른 컴퓨터들 탐색
            for (int i = 0; i < n; i++) {
                // 연결되어 있고, 아직 방문하지 않은 컴퓨터
                if (computers[c][i] == 1 && v[i] == 0) {  
                    v[i] = 1;  // 방문 표시
                    q.offer(i);  // 큐에 추가
                }
            }
        }
    }

    public int solution(int n, int[][] computers) {
        int answer = 0;
        v = new int[n];  // 방문 배열 초기화

        // 모든 컴퓨터에 대해 BFS 또는 DFS 탐색
        for (int i = 0; i < n; i++) {
            if (v[i] == 0) {  // 아직 방문하지 않은 컴퓨터에 대해 탐색 시작
                bfs(i, computers, n);
                answer++;  // 네트워크 개수 증가
            }
        }

        return answer;
    }
}
