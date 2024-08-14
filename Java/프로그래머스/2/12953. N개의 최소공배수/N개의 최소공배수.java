class Solution {
    public int solution(int[] arr) {
        // 초기 최소 공배수
        int temp = lcm(arr[0], arr[1]);

        // 모든 수와 공배수 계산
        for (int i = 2 ; i < arr.length ; i++) {
            temp = lcm(temp, arr[i]);
        }
        
        return temp;
    }

    // 최대공약수
    public int gcd (int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    // 최소공배수
    public int lcm (int a, int b) {
        return (a * b) / gcd(a , b);
    }
}