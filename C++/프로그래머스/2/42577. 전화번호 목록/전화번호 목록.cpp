#include <string>    
#include <vector>      
#include <algorithm>  

using namespace std;

// 전화번호 목록에서 접두어 관계가 있는지 확인하는 함수
bool solution(vector<string> phone_book) {
    // 1. 전화번호 목록을 사전순으로 정렬합니다.
    sort(phone_book.begin(), phone_book.end());

    // 2. 정렬된 전화번호 목록에서 인접한 전화번호끼리 접두어 관계인지 확인합니다.
    for(int i = 0; i < phone_book.size() - 1; i++) {
        // 0이 반환된 경우, 접두어로 판단
        if(phone_book[i + 1].find(phone_book[i]) == 0) {
            return false; 
        }
    }

    // 3. 모든 전화번호를 비교했을 때 접두어 관계가 없으면 true를 반환합니다.
    return true;
}
