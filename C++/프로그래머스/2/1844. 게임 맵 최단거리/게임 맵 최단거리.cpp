#include <vector>
#include <queue>

using namespace std;

// 상, 하, 좌, 우로 움직이기 위한 방향 벡터
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int solution(vector<vector<int>> maps) {
    int n = maps.size();       // 맵의 행 길이
    int m = maps[0].size();    // 맵의 열 길이
    
    // 방문 여부를 저장할 벡터
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    
    // BFS를 위한 큐 (x, y, 현재까지의 거리)
    queue<pair<int, int>> q;
    queue<int> distances;
    
    // 시작점(0, 0)을 큐에 넣고 방문 처리
    q.push({0, 0});
    distances.push(1);  // 시작점도 거리에 포함되므로 1부터 시작
    visited[0][0] = true;
    
    // BFS 탐색
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        int dist = distances.front();
        q.pop();
        distances.pop();
        
        // 목적지에 도착한 경우, 현재까지의 거리를 반환
        if (x == n - 1 && y == m - 1) {
            return dist;
        }
        
        // 상, 하, 좌, 우로 이동
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // 맵의 경계를 벗어나지 않고, 방문하지 않았으며, 갈 수 있는 길(1)인 경우
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && maps[nx][ny] == 1) {
                q.push({nx, ny});
                distances.push(dist + 1);  // 거리를 1 증가
                visited[nx][ny] = true;    // 방문 처리
            }
        }
    }
    
    // 목적지에 도착하지 못한 경우 -1 반환
    return -1;
}
