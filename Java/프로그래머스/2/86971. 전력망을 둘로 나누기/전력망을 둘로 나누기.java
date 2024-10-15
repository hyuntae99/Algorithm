import java.util.*;

class Solution {
    
    // BFS로 그래프 순회한 노드 수 반환
    public int bfs(Map<Integer, List<Integer>> graph, int start, boolean[] visited) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);  // 시작 노드를 큐에 추가
        visited[start] = true;  // 방문 처리
        int count = 1;  // 방문한 노드 수 초기화

        while (!q.isEmpty()) {
            int node = q.poll();  // 큐에서 노드를 꺼냄
            for (int adjacent : graph.get(node)) {  // 인접한 노드들을 순회
                if (!visited[adjacent]) {  // 방문하지 않은 노드만
                    visited[adjacent] = true;  // 방문 처리
                    q.offer(adjacent);  // 큐에 인접 노드를 추가
                    count++;  // 방문한 노드 수 증가
                }
            }
        }

        return count;  // 방문한 총 노드 수 반환
    }

    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;  // 결과값을 큰 값으로 초기화

        // 각 전선을 하나씩 제거하여 시뮬레이션
        for (int[] wireToCut : wires) {
            Map<Integer, List<Integer>> graph = new HashMap<>();  // 그래프 초기화

            // 그래프 초기화
            for (int i = 1; i <= n; i++) {
                graph.put(i, new ArrayList<>());  // 각 노드의 인접 리스트 생성
            }

            // 전선 그래프 생성
            for (int[] wire : wires) {
                if (Arrays.equals(wire, wireToCut)) {
                    continue;  // 자를 전선은 건너뜀
                }
                int a = wire[0];
                int b = wire[1];
                graph.get(a).add(b);  // 무방향 그래프이므로 양방향 연결
                graph.get(b).add(a);
            }

            // 한 쪽 서브트리 크기 계산 (시작 노드는 자른 전선의 한 쪽 노드)
            boolean[] visited = new boolean[n + 1];  // 노드 방문 여부 체크
            int n1 = bfs(graph, wireToCut[0], visited);  // 첫 번째 노드로부터 BFS 실행
            int n2 = n - n1;  // 전체에서 n1을 제외한 나머지 노드 수

            // 두 서브트리의 크기 차이를 계산
            answer = Math.min(answer, Math.abs(n1 - n2));
        }

        return answer;
    }
}
