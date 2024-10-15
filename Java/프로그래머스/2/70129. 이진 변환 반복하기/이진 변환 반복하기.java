class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2]; // [변환 횟수, 제거된 0의 개수]
        int transformCount = 0;    // 변환 횟수를 카운트
        int zeroCount = 0;         // 제거된 0의 개수 카운트

        // 문자열이 "1"이 될 때까지 반복
        while (!s.equals("1")) {
            transformCount++;  // 변환 횟수 증가

            // 현재 문자열에서 '0'을 제거
            int originalLength = s.length();
            s = s.replaceAll("0", "");  // '0'을 제거한 문자열
            int newLength = s.length();

            // 제거된 '0'의 개수를 더함
            zeroCount += (originalLength - newLength);

            // 남은 문자열의 길이를 2진수로 변환
            s = Integer.toBinaryString(newLength);
        }

        // 결과 저장
        answer[0] = transformCount;  // 변환 횟수
        answer[1] = zeroCount;       // 제거된 0의 총 개수

        return answer;
    }
}
