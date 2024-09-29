#include <string>          
#include <vector>          
#include <unordered_map>   
#include <iostream>

using namespace std;

int solution(vector<vector<string>> clothes) {
    // 1. 의상 종류별로 의상 개수를 저장할 해시 테이블 선언
    unordered_map<string, int> clothes_map;
    
    // 2. 모든 의상을 순회하며 각 종류별 개수 세기
    for(int i = 0; i < clothes.size(); i++) {
        string type = clothes[i][1]; // 의상 종류
        clothes_map[type] = clothes_map[type] + 1; // 해당 종류의 의상 개수 증가
    }
    
    // 3. 가능한 조합 수 계산
    int answer = 1;
    // 해시 테이블의 모든 요소를 순회
    for(pair<string, int> it : clothes_map) {
        // 각 의상 종류별로 (의상 개수 + 1)을 곱함
        // +1은 해당 종류의 의상을 선택하지 않는 경우를 포함
        cout << it.first << " " << it.second << endl;
        answer = answer * (it.second + 1);
    }
    
    // 4. 모든 종류에서 아무것도 선택하지 않는 경우를 제외
    answer = answer - 1;
    
    return answer;
}
