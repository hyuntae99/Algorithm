#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string word) {
    vector<char> vowels = {'A', 'E', 'I', 'O', 'U'};
    // 5^4 = 625, 5^3 = 125, 5^2 = 25, 5^1 = 5, 5^0 = 1
    vector<int> power = {781, 156, 31, 6, 1};  // 각 자리수에서 가능한 단어의 수

    int result = 0;
    
    // 주어진 단어의 각 문자의 위치를 계산
    for (int i = 0; i < word.size(); i++) {
        // 현재 문자가 vowels 벡터에서 몇 번째에 위치하는지 찾음
        for (int j = 0; j < 5; j++) {
            if (word[i] == vowels[j]) {
                // 위치에 따른 사전 순서를 계산
                result += power[i] * j + 1;
                break;
            }
        }
    }
    
    return result;
}
