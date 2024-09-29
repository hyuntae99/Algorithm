#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> persons;
    vector<int> person1 = {1,2,3,4,5};
    vector<int> person2 = {2,1,2,3,2,4,2,5};
    vector<int> person3 = {3,3,1,1,2,2,4,4,5,5};
    
    int answer1 = 0;
    int answer2 = 0;
    int answer3 = 0;
    
    // 각 수포자의 답을 독립적으로 검사
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == person1[i % person1.size()]) {
            answer1++;
        }
        if (answers[i] == person2[i % person2.size()]) {
            answer2++;
        }
        if (answers[i] == person3[i % person3.size()]) {
            answer3++;
        }
    }

    // 가장 많이 맞춘 사람을 찾음
    int maxScore = max({answer1, answer2, answer3});
    
    // 가장 많이 맞춘 사람을 persons 벡터에 넣음
    if (answer1 == maxScore) persons.push_back(1);
    if (answer2 == maxScore) persons.push_back(2);
    if (answer3 == maxScore) persons.push_back(3);
    
    return persons;
}
