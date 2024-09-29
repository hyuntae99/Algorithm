#include <string>
#include <vector>
#include <algorithm>   

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for (int i = 0; i < commands.size(); i++) {
        int start = commands[i][0] - 1;  // 시작 인덱스
        int end = commands[i][1];        // 끝 인덱스
        int k = commands[i][2] - 1;      // k번째 인덱스 

        // array에서 지정된 범위만큼 잘라내어 새로운 배열 생성
        vector<int> arr(array.begin() + start, array.begin() + end);

        // 잘라낸 배열 정렬
        sort(arr.begin(), arr.end());

        // k번째 숫자를 answer에 추가
        answer.push_back(arr[k]);
    }

    return answer;
}
