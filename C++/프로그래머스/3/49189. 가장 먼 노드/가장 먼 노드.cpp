#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    vector<vector<int>> graph(n + 1);  // 노드 연결 정보 저장
    vector<int> distance(n + 1, -1);   // 거리 저장 (-1은 방문하지 않음)
    
    // 간선 정보로 그래프 만들기
    for (auto& e : edge) {
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }
    
    // BFS 시작
    queue<int> q;
    q.push(1);  // 1번 노드부터 시작
    distance[1] = 0;  // 1번 노드는 거리가 0
    
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        
        // 현재 노드와 연결된 노드들을 확인
        for (int next : graph[cur]) {
            if (distance[next] == -1) {  // 방문하지 않은 노드만
                distance[next] = distance[cur] + 1;  // 최단 거리 계산
                q.push(next);
            }
        }
    }
    
    // 가장 큰 거리를 찾고, 그 거리에 해당하는 노드 개수 세기
    int max_dist = *max_element(distance.begin(), distance.end());
    return count(distance.begin(), distance.end(), max_dist);
}
