import java.util.*;

public class Main {
    static ArrayList<Integer>[] graph;   // 그래프를 저장할 인접 리스트
    static boolean[] visited;            // 방문 여부 체크
    static int count = 0;                // 감염된 컴퓨터 수

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // 컴퓨터 수 (정점의 수)
        int m = sc.nextInt();  // 연결 수 (간선의 수)

        // 그래프 초기화
        graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        // 간선 입력 받기
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        // 방문 배열 초기화
        visited = new boolean[n + 1];

        // DFS 실행 (1번 컴퓨터부터 시작)
        dfs(1);

        // 결과 출력 (1번 컴퓨터는 제외해야 하므로 -1)
        System.out.println(count - 1);
    }

    // DFS 함수
    public static void dfs(int node) {
        visited[node] = true;
        count++;  // 감염된 컴퓨터 수 증가

        // 인접한 노드들 탐색
        for (int next : graph[node]) {
            if (!visited[next]) {
                dfs(next);  // 재귀적으로 DFS 탐색
            }
        }
    }
}
