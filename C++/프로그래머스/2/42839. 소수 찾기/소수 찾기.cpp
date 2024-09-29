#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>

using namespace std;

// 소수 판별 함수
bool isPrime(int num) {
    if (num <= 1) return false;  // 1 이하는 소수가 아님
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;  // 나누어 떨어지면 소수가 아님
    }
    return true;  // 소수임
}

// 가능한 모든 순열을 생성하고 소수를 찾는 함수
int solution(string numbers) {
    set<int> uniqueNumbers;  // 중복을 피하기 위한 set
    
    // 모든 가능한 숫자 조합을 만들기 위한 순열 생성
    sort(numbers.begin(), numbers.end());
    
    // 모든 자릿수에 대해 순열을 생성
    do {
        for (int len = 1; len <= numbers.size(); len++) {
            int num = stoi(numbers.substr(0, len));  // 숫자로 변환
            uniqueNumbers.insert(num);  // 중복 없이 숫자 저장
        }
    } while (next_permutation(numbers.begin(), numbers.end()));

    // 소수 개수 세기
    int primeCount = 0;
    for (int num : uniqueNumbers) {
        if (isPrime(num)) {
            primeCount++;
        }
    }

    return primeCount;
}
