class Solution {
    public int solution(int n, int k) {
        // k진법 변환
        String num = "";
        while (n > 0) {
            num += n % k;
            n /= k;
        }
        // 역순으로 뒤집어서 변환
        String number = new StringBuilder(num).reverse().toString();
        
        // 0을 기준으로 숫자 나누기
        String[] parts = number.split("0");
        
        int count = 0;
        // 각 숫자에 대해 소수 여부를 확인
        for (String part : parts) {
            if (!part.equals("") && isPrime(Long.parseLong(part))) {
                count++;
            }
        }
        
        return count;
    }
    
    // 소수 판별 함수
    public boolean isPrime(long num) {
        // 1은 소수가 아니다.
        if (num < 2) {
            return false;
        }
        for (long i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}