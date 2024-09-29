#include <string>
#include <vector>
#include <algorithm> 
#include <iostream>

using namespace std;

// 던전을 탐험할 수 있는 순열을 확인하는 함수
int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;

    // 모든 순열을 확인하기 위해 던전을 정렬
    sort(dungeons.begin(), dungeons.end());

    do {
        int currentK = k;  // 현재 체력
        int clearedDungeons = 0;  // 탐험한 던전 수

        // 각 던전의 피로도를 확인
        for (int i = 0; i < dungeons.size(); i++) {
            if (currentK >= dungeons[i][0]) {  // 최소 필요 피로도를 만족할 경우
                currentK -= dungeons[i][1];  // 던전을 탐험하고 소모 피로도 차감
                clearedDungeons++;  // 탐험한 던전 수 증가
            } else {
                break;  // 더 이상 탐험할 수 없으면 종료
            }
        }

        // 가장 많이 탐험한 던전 수를 갱신
        answer = max(answer, clearedDungeons);

    } while (next_permutation(dungeons.begin(), dungeons.end()));  // 모든 순열을 탐험

    return answer;
}
