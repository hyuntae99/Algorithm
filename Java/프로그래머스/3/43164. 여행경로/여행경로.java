import java.util.*;

class Solution {
    boolean[] visited;  // 항공권 사용 여부를 체크하는 배열
    List<String> answer;  // 가능한 경로를 저장하는 리스트
    
    public boolean dfs(String current, String[][] tickets, List<String> route, int count) {
        // 모든 티켓을 사용한 경우 경로를 찾은 것이므로 true 반환
        if (count == tickets.length) {
            answer = new ArrayList<>(route);
            return true;
        }
        
        // 현재 위치에서 다음 목적지로 이동
        for (int i = 0; i < tickets.length; i++) {
            // 미방문 + 출발지여야 함
            if (!visited[i] && tickets[i][0].equals(current)) {
                visited[i] = true;  // 해당 티켓을 사용
                route.add(tickets[i][1]);  // 경로에 목적지 추가
                boolean found = dfs(tickets[i][1], tickets, route, count + 1);  
                if (found) {
                    return true;  // 경로를 찾았으면 바로 종료
                }
                visited[i] = false;  // 해당 티켓을 다시 사용하지 않도록 되돌림
                route.remove(route.size() - 1);  // 경로에서 마지막 목적지 제거
            }
        }
        return false;  // 모든 경로를 다 탐색한 후에도 경로를 찾지 못한 경우
    }
    
    public String[] solution(String[][] tickets) {
        // 항공권을 사전순으로 정렬
        Arrays.sort(tickets, (a, b) -> {
            if (a[0].equals(b[0])) {
                return a[1].compareTo(b[1]);  // 출발지가 같다면 도착지를 사전순 정렬
            }
            return a[0].compareTo(b[0]);  // 출발지를 사전순 정렬
        });
        
        visited = new boolean[tickets.length];  // 방문 체크 배열 초기화
        List<String> route = new ArrayList<>();  // 현재 경로를 저장할 리스트
        route.add("ICN");  // 시작점은 항상 "ICN"
        
        dfs("ICN", tickets, route, 0);  // DFS 탐색 시작
        
        // 리스트를 배열로 변환하여 반환
        return answer.toArray(new String[answer.size()]);
    }
}
