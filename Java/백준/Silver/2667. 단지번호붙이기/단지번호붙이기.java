import java.util.*;

public class Main {
    static int[][] map;  // 지도를 저장할 배열
    static boolean[][] visited;  // 방문 여부 체크
    static int N;  // 지도의 크기
    static int[] dx = {-1, 1, 0, 0};  // 상하좌우 이동을 위한 배열
    static int[] dy = {0, 0, -1, 1};  // 상하좌우 이동을 위한 배열
    static int count;  // 각 단지의 집 수

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();  // 지도의 크기
        map = new int[N][N];
        visited = new boolean[N][N];
        
        // 지도 입력 받기
        for (int i = 0; i < N; i++) {
            String line = sc.next();
            for (int j = 0; j < N; j++) {
                map[i][j] = line.charAt(j) - '0';  // '0'과 '1'을 숫자로 변환
            }
        }
        
        // 각 단지의 집 수를 저장할 리스트
        List<Integer> result = new ArrayList<>();
        
        // 모든 위치를 탐색하며 단지 찾기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {  // 집이 있고, 아직 방문하지 않았다면
                    count = 0;  // 새로운 단지를 찾았으므로 집 수 초기화
                    dfs(i, j);  // DFS로 단지 탐색
                    result.add(count);  // 단지의 집 수 저장
                }
            }
        }
        
        // 결과 정렬 후 출력
        Collections.sort(result);  // 오름차순 정렬
        System.out.println(result.size());  // 단지 수 출력
        for (int cnt : result) {
            System.out.println(cnt);  // 각 단지에 속한 집의 수 출력
        }
    }

    // DFS 함수
    public static void dfs(int x, int y) {
        visited[x][y] = true;
        count++;  // 현재 집을 포함시킴
        
        // 상하좌우 탐색
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // 지도 범위 안에 있고, 집이 있으며, 아직 방문하지 않았다면 DFS 호출
            if (nx >= 0 && nx < N && ny >= 0 && ny < N && map[nx][ny] == 1 && !visited[nx][ny]) {
                dfs(nx, ny);
            }
        }
    }
}
