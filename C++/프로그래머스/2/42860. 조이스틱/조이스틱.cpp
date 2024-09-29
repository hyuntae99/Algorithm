#include <string>
#include <vector>
#include <algorithm> 

using namespace std;

int solution(string name) {
    int n = name.length();
    int moveCount = 0; // 좌우 이동 횟수
    int answer = 0;    // 총 조작 횟수

    // 1. 각 문자를 'A'에서 원하는 문자로 바꾸는 횟수 계산 (위/아래 이동)
    for (int i = 0; i < n; i++) {
        // 'A'에서 해당 문자까지의 거리와 반대 방향으로의 거리를 비교하여 최소값을 취함
        answer += min(name[i] - 'A', 'Z' - name[i] + 1);
    }

    // 2. 좌우 이동 횟수 계산 (좌/우 이동)
    moveCount = n - 1;
    
    for (int i = 0; i < n; i++) {
        // 다음에 'A'가 아닌 문자를 만나는 가장 가까운 위치를 찾음
        int next = i + 1;
        while (next < n && name[next] == 'A') {
            next++;
        }

        // 현재 위치에서 다음 'A'가 아닌 문자까지 이동 후 다시 돌아오는 경우를 계산
        moveCount = min(moveCount, i + n - next + min(i, n - next));
    }

    return answer + moveCount;
}
