#include <vector>  

using namespace std;

// 같은 숫자는 싫어 문제를 해결하는 함수
vector<int> solution(vector<int> arr) {
    vector<int> answer;          // 결과를 저장할 벡터
    int previous = -1;           // 이전 숫자를 저장할 변수 

    // 입력 배열을 순회
    for(int i = 0; i < arr.size(); i++) {
        // 현재 숫자가 이전 숫자와 다르면
        if(arr[i] != previous) {
            answer.push_back(arr[i]);  // 결과 벡터에 추가
            previous = arr[i];         // 이전 숫자 업데이트
        }
    }

    return answer; // 최종 결과 반환
}
