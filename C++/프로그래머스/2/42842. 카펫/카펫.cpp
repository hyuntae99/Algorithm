#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;

    // 전체 타일 개수
    int total = brown + yellow;

    // 가로 길이 w, 세로 길이 h는 전체 타일의 약수 중에서 구할 수 있음
    for (int h = 3; h <= total; h++) {
        if (total % h == 0) {  // h가 total의 약수여야 함
            int w = total / h;  // w는 가로 길이
            
            // 갈색과 노란색 타일의 조건을 만족하는지 확인
            if ((w - 2) * (h - 2) == yellow) {
                answer.push_back(w);
                answer.push_back(h);
                return answer;
            }
        }
    }
    
    return answer;
}
