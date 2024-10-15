import java.util.*;

public class Main {
    static int[][] maze;  // 미로 배열
    static boolean[][] visited;  // 방문 여부 체크
    static int N, M;  // 미로의 크기
    static int[] dx = {-1, 1, 0, 0};  // 상하좌우 이동을 위한 배열
    static int[] dy = {0, 0, -1, 1};  // 상하좌우 이동을 위한 배열

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();  // 행 수
        M = sc.nextInt();  // 열 수

        maze = new int[N][M];
        visited = new boolean[N][M];

        // 미로 입력 받기
        for (int i = 0; i < N; i++) {
            String row = sc.next();
            for (int j = 0; j < M; j++) {
                maze[i][j] = row.charAt(j) - '0';  // '1' 또는 '0'을 숫자로 변환
            }
        }

        // BFS 탐색 시작
        int result = bfs(0, 0);
        System.out.println(result);
    }

    // BFS 함수
    public static int bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {x, y});
        visited[x][y] = true;

        // 큐가 빌 때까지 탐색
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int cx = current[0];
            int cy = current[1];

            // 도착 지점에 도달하면 그 위치의 값을 반환 (최단 경로)
            if (cx == N - 1 && cy == M - 1) {
                return maze[cx][cy];
            }

            // 상하좌우로 이동
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                // 미로 범위 안에 있고, 이동할 수 있는 칸이며, 방문하지 않은 경우
                if (nx >= 0 && nx < N && ny >= 0 && ny < M && maze[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    maze[nx][ny] = maze[cx][cy] + 1;  // 이전 칸에서 +1 이동
                    q.offer(new int[] {nx, ny});
                }
            }
        }

        return -1;  // 도달할 수 없는 경우는 없으므로 기본적으로 실행되지 않음
    }
}
