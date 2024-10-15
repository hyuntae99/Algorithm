import java.util.*;

public class Main {
    static int M, N, H;  // 가로, 세로, 높이
    static int[][][] box;  // 토마토 상자
    static boolean[][][] visited;  // 방문 여부 체크
    static int[] dx = {1, -1, 0, 0, 0, 0};  // 상하좌우 + 위아래 이동
    static int[] dy = {0, 0, 1, -1, 0, 0};
    static int[] dz = {0, 0, 0, 0, 1, -1};
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        M = sc.nextInt();  // 가로
        N = sc.nextInt();  // 세로
        H = sc.nextInt();  // 높이
        box = new int[H][N][M];  // 3차원 배열로 토마토 상자 초기화
        visited = new boolean[H][N][M];
        
        Queue<int[]> q = new LinkedList<>();
        
        // 입력 받기
        for (int z = 0; z < H; z++) {
            for (int y = 0; y < N; y++) {
                for (int x = 0; x < M; x++) {
                    box[z][y][x] = sc.nextInt();
                    if (box[z][y][x] == 1) { 
                        q.offer(new int[] {z, y, x});  // 익은 토마토 위치 저장
                        visited[z][y][x] = true;
                    }
                }
            }
        }
        
        // BFS 탐색
        int result = bfs(q);
        
        // 익지 않은 토마토가 남아 있는지 확인
        for (int z = 0; z < H; z++) {
            for (int y = 0; y < N; y++) {
                for (int x = 0; x < M; x++) {
                    if (box[z][y][x] == 0) {  // 익지 않은 토마토가 있다면
                        System.out.println(-1);
                        return;
                    }
                }
            }
        }
        
        System.out.println(result);  // 모든 토마토가 익었을 때 걸린 시간 출력
    }

    // BFS 함수
    public static int bfs(Queue<int[]> q) {
        int days = 0;  // 최종 소요 일수
        
        while (!q.isEmpty()) {
            int size = q.size();
            boolean hasRipened = false;
            
            for (int i = 0; i < size; i++) {
                int[] current = q.poll();
                int z = current[0];
                int y = current[1];
                int x = current[2];
                
                // 6방향으로 탐색 (상, 하, 좌, 우, 위, 아래)
                for (int dir = 0; dir < 6; dir++) {
                    int nz = z + dz[dir];
                    int ny = y + dy[dir];
                    int nx = x + dx[dir];
                    
                    // 범위를 벗어나지 않고, 익지 않은 토마토(0)인 경우
                    if (nz >= 0 && nz < H && ny >= 0 && ny < N && nx >= 0 && nx < M && box[nz][ny][nx] == 0 && !visited[nz][ny][nx]) {
                        visited[nz][ny][nx] = true;  // 방문 체크
                        box[nz][ny][nx] = 1;  // 익은 토마토로 변경
                        q.offer(new int[] {nz, ny, nx});  // 큐에 새 위치 추가
                        hasRipened = true;  // 익은 토마토가 있었음을 표시
                    }
                }
            }
            
            if (hasRipened) {
                days++;  // 하루가 지난 것으로 계산
            }
        }
        
        return days;
    }
}
