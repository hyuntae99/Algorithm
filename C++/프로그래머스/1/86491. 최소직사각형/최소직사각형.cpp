#include <vector>
#include <algorithm>  

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_width = 0;   // 긴 변의 최대값
    int max_height = 0;  // 짧은 변의 최대값
    
    // 각 명함에 대해 가로와 세로 중 큰 값과 작은 값을 결정
    for (int i = 0; i < sizes.size(); i++) {
        // 두 값 중 큰 값은 긴 변, 작은 값은 짧은 변
        int big = max(sizes[i][0], sizes[i][1]);
        int small = min(sizes[i][0], sizes[i][1]);
        
        // 긴 변 중 최대값과 짧은 변 중 최대값을 구함
        max_width = max(max_width, big);
        max_height = max(max_height, small);
    }
    
    // 가장 긴 변과 가장 짧은 변을 곱한 값이 지갑의 최소 크기
    return max_width * max_height;
}
