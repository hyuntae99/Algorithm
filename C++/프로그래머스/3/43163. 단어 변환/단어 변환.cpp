#include <string>
#include <vector>
#include <queue>
#include <algorithm> 

using namespace std;

// 두 단어가 한 글자만 다를 경우 true 반환
bool canTransform(const string& word1, const string& word2) {
    int diffCount = 0;
    for (int i = 0; i < word1.size(); i++) {
        if (word1[i] != word2[i]) {
            diffCount++;
        }
        if (diffCount > 1) {
            return false;
        }
    }
    return diffCount == 1;
}

int solution(string begin, string target, vector<string> words) {
    // target이 words에 없으면 변환 불가능
    if (find(words.begin(), words.end(), target) == words.end()) {
        return 0;
    }

    // BFS 탐색을 위한 큐
    queue<pair<string, int>> q;
    q.push({begin, 0});  // 시작 단어는 변환 횟수가 0

    // words에 있는 단어의 방문 여부를 확인하기 위한 벡터
    vector<bool> visited(words.size(), false);

    // BFS 탐색
    while (!q.empty()) {
        string currentWord = q.front().first;
        int currentCount = q.front().second;
        q.pop();

        // 목표 단어에 도달하면 현재 변환 횟수 반환
        if (currentWord == target) {
            return currentCount;
        }

        // words 리스트를 순회하면서 변환 가능한 단어를 찾음
        for (int i = 0; i < words.size(); i++) {
            if (!visited[i] && canTransform(currentWord, words[i])) {
                visited[i] = true;  // 해당 단어를 방문 처리
                q.push({words[i], currentCount + 1});  // 변환 후 큐에 넣음
            }
        }
    }

    // target으로 변환할 수 없을 경우 0 반환
    return 0;
}
