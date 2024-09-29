#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long left = 1;
    long long right = *max_element(times.begin(), times.end()) * (long long)n;

    while (left <= right) {
        long long mid = (left + right) / 2;
        long long total = 0;
        
        // mid 시간 동안 각 심사관이 몇 명을 처리할 수 있는지 계산
        for (int time : times) {
            total += mid / time;
        }

        if (total >= n) {
            answer = mid;  // 더 짧은 시간으로도 가능할 수 있으므로 답 갱신
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return answer;
}
