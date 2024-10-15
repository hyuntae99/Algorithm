import java.util.*;

class Solution {
    public int solution(int N, int number) {
        if (N == number) {
            return 1;  // N과 number가 같으면 바로 1 반환
        }

        // DP 배열: i번째 index에는 N을 i번 사용해서 만들 수 있는 숫자들의 집합이 저장됨
        List<Set<Integer>> dp = new ArrayList<>();

        // DP 배열 초기화
        for (int i = 0; i <= 8; i++) {
            dp.add(new HashSet<>());
        }

        // N을 i번 반복해서 만든 숫자를 초기값으로 넣어줌 (예: 5 -> 55 -> 555 ...)
        for (int i = 1; i <= 8; i++) {
            String repeatedN = String.valueOf(N).repeat(i);
            dp.get(i).add(Integer.parseInt(repeatedN));
        }

        // 동적 계획법으로 사칙연산 수행
        for (int i = 1; i <= 8; i++) {
            for (int j = 1; j < i; j++) {
                for (int a : dp.get(j)) {
                    for (int b : dp.get(i - j)) {
                        dp.get(i).add(a + b);
                        dp.get(i).add(a - b);
                        dp.get(i).add(a * b);
                        if (b != 0) {
                            dp.get(i).add(a / b);
                        }
                    }
                }
            }

            // 목표 숫자를 만들 수 있는 경우
            if (dp.get(i).contains(number)) {
                return i;  // 해당 횟수 반환
            }
        }

        return -1;  // 8번 이하로 목표 숫자를 만들 수 없을 경우 -1 반환
    }
}
