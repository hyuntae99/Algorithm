import java.util.*;

class Solution {
    Set<Integer> primeNumbers = new HashSet<>();  // 중복을 방지하기 위한 Set

    public int solution(String numbers) {
        // 주어진 문자열로 가능한 모든 숫자 조합을 구하기 위한 처리
        char[] numArr = numbers.toCharArray();
        boolean[] v = new boolean[numArr.length];

        // 모든 자릿수의 순열을 구하여 소수 판별
        for (int i = 1; i <= numArr.length; i++) {
            dfs(numArr, v, "", i);
        }

        // 소수 개수 반환
        return primeNumbers.size();
    }

    // 순열을 구하는 함수
    private void dfs(char[] numArr, boolean[] v, String current, int length) {
        if (current.length() == length) { // 자릿수 만족
            int number = Integer.parseInt(current);  // 숫자로 변환
            if (isPrime(number)) {
                primeNumbers.add(number);  // 소수라면 Set에 추가하여 중복 방지
            }
            return;
        }

        for (int i = 0; i < numArr.length; i++) {
            if (!v[i]) { // 미방문
                v[i] = true;
                dfs(numArr, v, current + numArr[i], length); // 백트래킹
                v[i] = false;  
            }
        }
    }

    // 소수 판별 함수
    private boolean isPrime(int num) {
        if (num < 2) {
            return false;  // 0과 1은 소수가 아님
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;  // 나누어 떨어지면 소수가 아님
            }
        }
        return true;
    }
}
